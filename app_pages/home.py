import streamlit as st
from app_core.data import csv

studies=csv("literature/master_studies.csv")
status=csv("literature/complete_status.csv")
work=csv("literature/pending_work.csv")

st.title("MANET Routing Evidence Atlas")
st.caption("An interactive, evidence-centered map of mobile ad hoc network routing research.")

st.markdown("""
This atlas organizes MANET routing by **decision mechanism, information requirements, operating conditions,
evidence maturity, reproducibility, comparability, and demonstrated limitations**. It deliberately separates
published claims from controlled Observatory evidence.
""")

c1,c2,c3,c4=st.columns(4)
c1.metric("Registered studies", len(studies))
c2.metric("Algorithms/status records", len(status))
v2=sum(studies.get("verification_state",[]).isin(["V2","V3","V4"])) if not studies.empty else 0
c3.metric("V2+ verified sources", int(v2))
open_p0=sum((work["priority"]=="P0") & (~work["status"].isin(["complete","waived"]))) if not work.empty else 0
c4.metric("Open P0 research gates", int(open_p0))

st.subheader("How to read the atlas")
st.markdown("""
**Algorithm Explorer** answers *what a routing mechanism does and what it costs*.  
**Evidence Explorer** answers *what the literature actually establishes*.  
**Benchmark Observatory** answers *what happens under a common controlled evaluation*.  
**Gaps & Obligations** distinguishes sparse literature from experimentally demonstrated capability gaps.  
**Methodology** exposes the rules used to admit, compare, and interpret evidence.
""")

st.warning("The atlas is a living research artifact. Missing evidence is shown as missing; it is never inferred.")
