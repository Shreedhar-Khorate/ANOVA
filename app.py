"""
ANOVA Analysis Tool - Main Application
Engineering Mathematics-4 Project | Group 12
Advanced Website-Style Interface with Navbar
"""

import streamlit as st
from config import APP_TITLE, APP_ICON, APP_LAYOUT
from components import render_navbar
from pages import show_home, show_analysis, show_results, show_about


# ─── Page Configuration ──────────────────────────────────
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
)


# ─── Initialize Session State ────────────────────────────
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"


# ─── Render Navbar (Top Level - Only Once) ──────────────
render_navbar()


# ─── Route to Appropriate Page ───────────────────────────
if st.session_state.current_page == "home":
    show_home()
elif st.session_state.current_page == "analysis":
    show_analysis()
elif st.session_state.current_page == "results":
    show_results()
elif st.session_state.current_page == "about":
    show_about()
