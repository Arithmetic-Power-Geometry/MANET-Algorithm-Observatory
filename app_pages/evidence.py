import streamlit as st
from app_core.data import csv

st.title("Evidence Explorer")
studies=csv("literature/master_studies.csv")
evidence=csv("literature/classical_evidence_v3.csv")

st.markdown("Explore verified studies separately from structured evidence claims.")

if not studies.empty:
    c1,c2,c3=st.columns(3)
    scope=c1.selectbox("Scope",["All"]+sorted(studies["scope"].unique().tolist()))
    state=c2.selectbox("Verification",["All","V0","V1","V2","V3","V4"])
    role=c3.selectbox("Study type",["All"]+sorted(studies["study_type"].unique().tolist()))
    q=studies.copy()
    if scope!="All": q=q[q["scope"]==scope]
    if state!="All": q=q[q["verification_state"]==state]
    if role!="All": q=q[q["study_type"]==role]
    st.dataframe(q, use_container_width=True, hide_index=True)

st.subheader("Structured evidence")
if evidence.empty:
    st.info("V3 evidence extraction is still in progress.")
else:
    algs=sorted(set(";".join(evidence["algorithm"]).split(";")))
    alg=st.selectbox("Filter evidence by algorithm",["All"]+algs)
    q=evidence if alg=="All" else evidence[evidence["algorithm"].str.contains(alg,regex=False)]
    st.dataframe(q, use_container_width=True, hide_index=True)
