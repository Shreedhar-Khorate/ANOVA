"""
components/navbar.py - Advanced Navigation Bar Component
"""

import streamlit as st
from config import APP_TITLE, PRIMARY_COLOR, PRIMARY_DARK


def render_navbar():
    """
    Render an advanced horizontal navigation bar.
    """
    
    # Custom CSS for navbar
    navbar_css = f"""
    <style>
    [data-testid="stSidebar"] {{
        display: none;
    }}
    
    .navbar {{
        position: sticky;
        top: 0;
        z-index: 1000;
        background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, {PRIMARY_DARK} 100%);
        padding: 0;
        margin: 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        backdrop-filter: blur(10px);
    }}
    
    .navbar-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px clamp(1rem, 4vw, 2rem);
        max-width: 100%;
        gap: clamp(0.5rem, 2vw, 1rem);
    }}
    
    .navbar-brand {{
        display: flex;
        align-items: center;
        gap: clamp(0.5rem, 1vw, 0.8rem);
        color: white;
        font-size: clamp(1rem, 3vw, 1.3rem);
        font-weight: 700;
        text-decoration: none;
        margin-right: auto;
        white-space: nowrap;
        min-width: fit-content;
    }}
    
    .navbar-menu {{
        display: flex;
        gap: clamp(0.3rem, 1vw, 0.5rem);
        align-items: center;
        list-style: none;
        margin: 0;
        padding: 0;
        flex-wrap: nowrap;
    }}
    
    .navbar-item {{
        text-align: center;
        transition: all 0.3s ease;
        flex-shrink: 0;
    }}
    
    .navbar-link {{
        color: white;
        text-decoration: none;
        padding: clamp(0.6rem, 1.5vw, 0.75rem) clamp(0.6rem, 1.5vw, 1rem);
        display: block;
        font-size: clamp(0.7rem, 2vw, 0.9rem);
        font-weight: 500;
        transition: all 0.3s ease;
        position: relative;
        border-radius: 6px;
        cursor: pointer;
        white-space: nowrap;
    }}
    
    .navbar-link:hover {{
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-1px);
    }}
    
    .navbar-link.active {{
        background-color: rgba(255, 255, 255, 0.3);
        border-bottom: 2px solid white;
    }}
    
    @media (max-width: 768px) {{
        .navbar-container {{
            padding: 10px clamp(0.8rem, 3vw, 1.2rem);
            gap: clamp(0.3rem, 1vw, 0.5rem);
        }}
        
        .navbar-brand {{
            font-size: clamp(0.9rem, 2.5vw, 1.1rem);
            gap: 0.4rem;
        }}
        
        .navbar-link {{
            padding: clamp(0.5rem, 1vw, 0.6rem) clamp(0.4rem, 1vw, 0.8rem);
            font-size: clamp(0.65rem, 1.5vw, 0.8rem);
            border-radius: 4px;
        }}
    }}
    
    @media (max-width: 480px) {{
        .navbar-container {{
            padding: 8px clamp(0.6rem, 2vw, 1rem);
            gap: 0.2rem;
        }}
        
        .navbar-brand {{
            font-size: clamp(0.8rem, 2vw, 0.95rem);
            gap: 0.3rem;
        }}
        
        .navbar-link {{
            padding: clamp(0.45rem, 0.8vw, 0.55rem) clamp(0.35rem, 0.8vw, 0.6rem);
            font-size: clamp(0.6rem, 1.2vw, 0.7rem);
            border-radius: 3px;
        }}
    }}
    </style>
    """
    
    # Inject CSS
    st.markdown(navbar_css, unsafe_allow_html=True)
    
    # Callback functions for navigation
    def go_to_home():
        st.session_state.current_page = "home"
    
    def go_to_analysis():
        st.session_state.current_page = "analysis"
    
    def go_to_results():
        st.session_state.current_page = "results"
    
    def go_to_about():
        st.session_state.current_page = "about"
    
    # Create navbar with columns
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([1.5, 1.2, 1.2, 1.2, 0.8])
    
    # Brand/Logo
    with nav_col1:
        st.markdown(f"## 📊 {APP_TITLE}", help="Click to go to home")
    
    # Navigation items with callbacks
    with nav_col2:
        st.button("🏠 Home", on_click=go_to_home, use_container_width=True)
    
    with nav_col3:
        st.button("📊 Analysis", on_click=go_to_analysis, use_container_width=True)
    
    with nav_col4:
        st.button("📈 Results", on_click=go_to_results, use_container_width=True)
    
    with nav_col5:
        st.button("ℹ️ About", on_click=go_to_about, use_container_width=True)
    
    # Add divider
    st.divider()


def get_page_icon(page_name):
    """Get icon for page."""
    icons = {
        "home": "🏠",
        "analysis": "📊",
        "results": "📈",
        "about": "ℹ️"
    }
    return icons.get(page_name, "")
