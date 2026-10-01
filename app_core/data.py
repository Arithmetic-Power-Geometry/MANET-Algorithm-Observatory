from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]

@st.cache_data
def csv(relpath: str) -> pd.DataFrame:
    path = ROOT / relpath
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, keep_default_na=False)

def metric(label, value, help_text=None):
    st.metric(label, value, help=help_text)

def empty_notice(name):
    st.info(f"{name} is not yet populated. The app exposes only repository evidence that currently exists.")
