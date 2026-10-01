import streamlit as st
from app_core.data import csv

st.title("Benchmark Observatory")
prov=csv("benchmark/IMPLEMENTATION_PROVENANCE.csv")
smoke=csv("benchmark/smoke_test_status.csv")
scenarios=csv("benchmark/TIER1_SCENARIO_DESIGN.csv")
metrics=csv("benchmark/METRIC_DICTIONARY.csv")

st.markdown("""
The controlled benchmark is reported independently of heterogeneous published performance claims.
Admission depends on implementation provenance and measurement validity.
""")

st.subheader("Implementation provenance")
st.dataframe(prov, use_container_width=True, hide_index=True)

st.subheader("Tier-1 smoke-test gate")
st.dataframe(smoke, use_container_width=True, hide_index=True)
if not smoke.empty and all(smoke["overall"]=="pass"):
    st.success("Large benchmark gate: OPEN")
else:
    st.warning("Large benchmark gate: CLOSED")

st.subheader("Scenario design")
st.dataframe(scenarios, use_container_width=True, hide_index=True)
st.subheader("Metric dictionary")
st.dataframe(metrics, use_container_width=True, hide_index=True)
