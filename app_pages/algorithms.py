import streamlit as st
from app_core.data import csv

st.title("Algorithm Explorer")
df=csv("literature/complete_status.csv")
if df.empty:
    st.info("Algorithm status records are not yet available.")
    st.stop()

families=sorted(x for x in df["family"].unique() if x)
family=st.selectbox("Routing family", ["All"]+families)
view=df if family=="All" else df[df["family"]==family]

names=view["algorithm_name"].tolist()
choice=st.selectbox("Algorithm / protocol", names)
row=view[view["algorithm_name"]==choice].iloc[0]

st.header(choice)
a,b,c=st.columns(3)
a.metric("First year", row.get("first_year","—"))
b.metric("Temporal mode", row.get("temporal_mode","—"))
c.metric("Benchmark admission", row.get("benchmark_admission","—"))

for heading, fields in [
    ("Decision and mechanism", ["decision_role","information_scope","control_mechanism"]),
    ("Capability and cost", ["main_capability","known_cost"]),
    ("Evidence status", ["simulation_evidence","testbed_evidence","field_evidence","reproducibility_status","generalization_status"]),
    ("Known limitations", ["known_failure_modes","contradiction_status","gap_tags"]),
]:
    st.subheader(heading)
    for f in fields:
        val=row.get(f,"")
        if val:
            st.markdown(f"**{f.replace('_',' ').title()}:** {val}")

with st.expander("Full structured status record"):
    st.dataframe(view[view["algorithm_name"]==choice], use_container_width=True, hide_index=True)
