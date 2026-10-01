import streamlit as st

st.set_page_config(
    page_title="MANET Routing Evidence Atlas",
    page_icon="📡",
    layout="wide",
)

pages = {
    "Atlas": [
        st.Page("app_pages/home.py", title="Evidence Atlas", icon=":material/hub:", default=True),
        st.Page("app_pages/algorithms.py", title="Algorithm Explorer", icon=":material/account_tree:"),
        st.Page("app_pages/evidence.py", title="Evidence Explorer", icon=":material/library_books:"),
    ],
    "Evaluation": [
        st.Page("app_pages/benchmark.py", title="Benchmark Observatory", icon=":material/science:"),
        st.Page("app_pages/gaps.py", title="Gaps & Obligations", icon=":material/troubleshoot:"),
    ],
    "Research": [
        st.Page("app_pages/methodology.py", title="Methodology", icon=":material/rule:"),
        st.Page("app_pages/reproducibility.py", title="Reproducibility", icon=":material/verified:"),
    ],
}
pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
