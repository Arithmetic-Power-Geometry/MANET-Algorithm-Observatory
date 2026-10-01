import streamlit as st
from app_core.data import csv

st.title("Reproducibility and Research Readiness")
work=csv("literature/pending_work.csv")

st.markdown("""
The paper is written only after the evidence package is frozen. This page exposes the same readiness state used by
the repository rather than presenting the project as complete prematurely.
""")
if not work.empty:
    status=st.multiselect("Status",sorted(work["status"].unique()),default=sorted(work["status"].unique()))
    q=work[work["status"].isin(status)]
    st.dataframe(q, use_container_width=True, hide_index=True)
    open_p0=q[(q["priority"]=="P0") & (~q["status"].isin(["complete","waived"]))]
    if len(open_p0):
        st.warning(f"Paper drafting gate: CLOSED — {len(open_p0)} visible P0 tasks remain open.")
    else:
        st.success("Paper drafting gate: OPEN for the currently selected records.")
