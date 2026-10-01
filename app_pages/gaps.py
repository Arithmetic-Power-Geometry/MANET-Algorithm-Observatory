import streamlit as st
from app_core.data import csv

st.title("Evidence Gaps and Research Obligations")
gaps=csv("literature/gap_registry.csv")
ob=csv("literature/research_obligations.csv")

st.markdown("""
A sparse literature region is not automatically a capability gap. The atlas distinguishes literature,
reproducibility, evaluation, contradiction, robustness, generalization, cost, real-world, and demonstrated
capability gaps.
""")
st.subheader("Gap registry")
st.dataframe(gaps, use_container_width=True, hide_index=True)
st.subheader("Research obligations")
st.dataframe(ob, use_container_width=True, hide_index=True)
