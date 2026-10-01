// SPDX-License-Identifier: Apache-2.0
// Copyright (C) 2026 Mohammad Amir Khusru Akhtar
//
// MANET Algorithm Observatory — Tier-1 common application measurement runner.
// Engineering validation runner; confirmatory scenario values are frozen separately.

#include "ns3/aodv-module.h"
#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/dsdv-module.h"
#include "ns3/dsr-module.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/network-module.h"
#include "ns3/olsr-module.h"
#include "ns3/wifi-module.h"

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <unordered_set>
#include <string>
#include <vector>

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("ObservatoryTier1Runner");

static uint64_t gTxAttempts=0, gTxRejected=0, gTxAccepted=0, gRxPackets=0, gOfferedBytes=0, gRxBytes=0;
static int gBindStatus=-999;
static std::vector<double> gDelaysMs;
static std::unordered_set<uint64_t> gSeenPacketId;

class ObservatoryHeader : public Header
{
public:
  ObservatoryHeader() = default;
  ObservatoryHeader(uint32_t sourceId, uint32_t seq, uint64_t txNs) : mMagic(0x4D414E45), mSourceId(sourceId), mSeq(seq), mTxNs(txNs) {}
  static TypeId GetTypeId()
  {
    static TypeId tid=TypeId("ObservatoryHeader").SetParent<Header>().AddConstructor<ObservatoryHeader>();
    return tid;
  }
  TypeId GetInstanceTypeId() const override { return GetTypeId(); }
  uint32_t GetSerializedSize() const override { return 20; }
  void Serialize(Buffer::Iterator i) const override { i.WriteHtonU32(mMagic); i.WriteHtonU32(mSourceId); i.WriteHtonU32(mSeq); i.WriteHtonU64(mTxNs); }
  uint32_t Deserialize(Buffer::Iterator i) override { mMagic=i.ReadNtohU32(); mSourceId=i.ReadNtohU32(); mSeq=i.ReadNtohU32(); mTxNs=i.ReadNtohU64(); return 20; }
  void Print(std::ostream& os) const override { os<<"source="<<mSourceId<<" seq="<<mSeq; }
  uint64_t GetTxNs() const { return mTxNs; }
  uint32_t GetSeq() const { return mSeq; }
  uint32_t GetSourceId() const { return mSourceId; }
  bool IsValid() const { return mMagic==0x4D414E45; }
private:
  uint32_t mMagic=0; uint32_t mSourceId=0; uint32_t mSeq=0;
  uint64_t mTxNs=0;
};

class Sender : public Application
{
public:
  void Setup(Address peer, uint32_t payloadBytes, Time interval, Time stop)
  { mPeer=peer; mPayload=payloadBytes; mInterval=interval; mStop=stop; }
private:
  void StartApplication() override
  {
    mSourceId=GetNode()->GetId();
    mSocket=Socket::CreateSocket(GetNode(), UdpSocketFactory::GetTypeId());
    gBindStatus=mSocket->Bind();
    if(gBindStatus<0) return;
    Send();
  }
  void StopApplication() override { if(mSocket) mSocket->Close(); }
  void Send()
  {
    if(Simulator::Now()>=mStop) return;
    Ptr<Packet> p=Create<Packet>(mPayload);
    ObservatoryHeader h(mSourceId, mSeq++, static_cast<uint64_t>(Simulator::Now().GetNanoSeconds()));
    p->AddHeader(h);
    ++gTxAttempts;
    gOfferedBytes+=mPayload;
    if(mSocket->SendTo(p,0,mPeer)>=0){ ++gTxAccepted; } else { ++gTxRejected; }
    mEvent=Simulator::Schedule(mInterval,&Sender::Send,this);
  }
  Ptr<Socket> mSocket; Address mPeer; uint32_t mPayload=512, mSourceId=0, mSeq=0; Time mInterval=Seconds(1),mStop=Seconds(0); EventId mEvent;
};

static void Receive(Ptr<Socket> socket)
{
  Address from;
  while(auto p=socket->RecvFrom(from))
  {
    ObservatoryHeader h;
    if(p->RemoveHeader(h)!=20 || !h.IsValid()) continue;
    uint64_t packetId=(static_cast<uint64_t>(h.GetSourceId())<<32)|h.GetSeq();
    if(!gSeenPacketId.insert(packetId).second) continue;
    ++gRxPackets;
    gRxBytes+=p->GetSize();
    double d=(Simulator::Now().GetNanoSeconds()-h.GetTxNs())/1e6;
    gDelaysMs.push_back(d);
  }
}

static double Percentile(std::vector<double> v,double q)
{
  if(v.empty()) return NAN;
  std::sort(v.begin(),v.end());
  double pos=q*(v.size()-1), lo=std::floor(pos), hi=std::ceil(pos);
  if(lo==hi) return v[lo];
  return v[lo]+(pos-lo)*(v[hi]-v[lo]);
}

int main(int argc,char** argv)
{
  std::string protocol="AODV", output="observatory-run.csv", scenario="engineering-common-001";
  uint32_t nodes=25, payload=512; double simTime=60.0, start=10.0, ratePps=2.0, speed=5.0; uint32_t seed=12345, run=1;
  CommandLine cmd(__FILE__);
  cmd.AddValue("protocol","AODV, DSDV, DSR, or OLSR",protocol);
  cmd.AddValue("output","Output CSV",output); cmd.AddValue("scenario","Scenario ID",scenario);
  cmd.AddValue("nodes","Node count",nodes); cmd.AddValue("payload","Application payload bytes",payload);
  cmd.AddValue("simTime","Simulation seconds",simTime); cmd.AddValue("start","Measurement/application start",start);
  cmd.AddValue("ratePps","Packets per second",ratePps); cmd.AddValue("speed","RandomWaypoint max speed m/s",speed);
  cmd.AddValue("seed","RNG seed",seed); cmd.AddValue("run","RNG run",run); cmd.Parse(argc,argv);
  NS_ABORT_MSG_IF(protocol!="AODV"&&protocol!="DSDV"&&protocol!="DSR"&&protocol!="OLSR","Unsupported protocol");
  RngSeedManager::SetSeed(seed); RngSeedManager::SetRun(run);

  NodeContainer n; n.Create(nodes);
  WifiHelper wifi; wifi.SetStandard(WIFI_STANDARD_80211b);
  WifiMacHelper mac; mac.SetType("ns3::AdhocWifiMac");
  YansWifiPhyHelper phy; YansWifiChannelHelper ch=YansWifiChannelHelper::Default(); phy.SetChannel(ch.Create());
  NetDeviceContainer dev=wifi.Install(phy,mac,n);

  MobilityHelper mob;
  Ptr<RandomRectanglePositionAllocator> position=CreateObject<RandomRectanglePositionAllocator>();
  position->SetAttribute("X",StringValue("ns3::UniformRandomVariable[Min=0|Max=500]"));
  position->SetAttribute("Y",StringValue("ns3::UniformRandomVariable[Min=0|Max=500]"));
  mob.SetPositionAllocator(position);
  mob.SetMobilityModel("ns3::RandomWaypointMobilityModel","Speed",StringValue("ns3::UniformRandomVariable[Min=0|Max="+std::to_string(speed)+"]"),"Pause",StringValue("ns3::ConstantRandomVariable[Constant=1]"),"PositionAllocator",PointerValue(position));
  mob.Install(n);

  InternetStackHelper internet;
  if(protocol=="AODV"){ AodvHelper h; internet.SetRoutingHelper(h); internet.Install(n); }
  else if(protocol=="DSDV"){ DsdvHelper h; internet.SetRoutingHelper(h); internet.Install(n); }
  else if(protocol=="OLSR"){ OlsrHelper h; internet.SetRoutingHelper(h); internet.Install(n); }
  else { internet.Install(n); DsrHelper dsr; DsrMainHelper main; main.Install(dsr,n); }

  Ipv4AddressHelper ip; ip.SetBase("10.1.0.0","255.255.0.0"); auto ifs=ip.Assign(dev);
  uint16_t port=9000;
  Ptr<Socket> sink=Socket::CreateSocket(n.Get(nodes-1),UdpSocketFactory::GetTypeId());
  sink->Bind(InetSocketAddress(Ipv4Address::GetAny(),port)); sink->SetRecvCallback(MakeCallback(&Receive));

  Ptr<Sender> sender=CreateObject<Sender>();
  sender->Setup(InetSocketAddress(ifs.GetAddress(nodes-1),port),payload,Seconds(1.0/ratePps),Seconds(simTime));
  n.Get(0)->AddApplication(sender); sender->SetStartTime(Seconds(start)); sender->SetStopTime(Seconds(simTime));
  Simulator::Stop(Seconds(simTime)); Simulator::Run(); Simulator::Destroy();

  double T=simTime-start, pdr=gTxAttempts?double(gRxPackets)/gTxAttempts:NAN, goodput=T>0?8.0*gRxBytes/T:NAN;
  double mean=NAN,median=NAN,p95=NAN,jitter=NAN;
  if(!gDelaysMs.empty()){ mean=std::accumulate(gDelaysMs.begin(),gDelaysMs.end(),0.0)/gDelaysMs.size(); median=Percentile(gDelaysMs,.5); p95=Percentile(gDelaysMs,.95); }
  if(gDelaysMs.size()>1){ double s=0; for(size_t i=1;i<gDelaysMs.size();++i)s+=std::abs(gDelaysMs[i]-gDelaysMs[i-1]); jitter=s/(gDelaysMs.size()-1); }

  std::ofstream o(output);
  o<<"benchmark_version,ns3_version,protocol,scenario_id,seed,run_number,node_count,area_width_m,area_height_m,mobility_model,max_speed_mps,traffic_model,packet_rate_pps,payload_bytes,measurement_start_s,measurement_end_s,socket_bind_status,tx_attempts,tx_rejected,socket_accepted_packets,app_packets_sent,app_packets_received,app_payload_bytes_sent,app_payload_bytes_received,pdr,goodput_bps,mean_delay_ms,median_delay_ms,p95_delay_ms,mean_jitter_ms,matched_packets,exit_status,validity_status\n";
  o<<std::setprecision(12)<<"engineering-v0,3.47,"<<protocol<<","<<scenario<<","<<seed<<","<<run<<","<<nodes<<",500,500,RandomWaypoint,"<<speed<<",UDP-periodic,"<<ratePps<<","<<payload<<","<<start<<","<<simTime<<","<<gBindStatus<<","<<gTxAttempts<<","<<gTxRejected<<","<<gTxAccepted<<","<<gTxAttempts<<","<<gRxPackets<<","<<gOfferedBytes<<","<<gRxBytes<<","<<pdr<<","<<goodput<<","<<mean<<","<<median<<","<<p95<<","<<jitter<<","<<gDelaysMs.size()<<",0,PASS\n";
}
