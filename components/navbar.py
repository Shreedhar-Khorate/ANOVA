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
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .navbar-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px clamp(1rem, 4vw, 2.5rem);
        max-width: 100%;
        gap: clamp(0.8rem, 2vw, 1.5rem);
        transition: all 0.3s ease;
    }}
    
    .navbar-brand {{
        display: flex;
        align-items: center;
        gap: clamp(0.6rem, 1vw, 1rem);
        color: white;
        font-size: clamp(1.1rem, 3vw, 1.5rem);
        font-weight: 800;
        text-decoration: none;
        margin-right: auto;
        white-space: nowrap;
        min-width: fit-content;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }}
    
    .navbar-brand:hover {{
        transform: scale(1.05);
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}
    
    .navbar-menu {{
        display: flex;
        gap: clamp(0.4rem, 1vw, 0.8rem);
        align-items: center;
        list-style: none;
        margin: 0;
        padding: 0;
        flex-wrap: nowrap;
    }}
    
    .navbar-item {{
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        flex-shrink: 0;
    }}
    
    .navbar-link {{
        color: white;
        text-decoration: none;
        padding: clamp(0.65rem, 1.5vw, 0.85rem) clamp(0.75rem, 1.5vw, 1.2rem);
        display: block;
        font-size: clamp(0.8rem, 2vw, 0.95rem);
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        border-radius: 8px;
        cursor: pointer;
        white-space: nowrap;
        overflow: hidden;
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .navbar-link::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }}
    
    .navbar-link::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.8), transparent);
        transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    .navbar-link:hover {{
        background-color: rgba(255, 255, 255, 0.15);
        border-color: rgba(255, 255, 255, 0.25);
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }}
    
    .navbar-link:hover::before {{
        left: 100%;
    }}
    
    .navbar-link:hover::after {{
        width: 100%;
    }}
    
    .navbar-link:active {{
        transform: translateY(-1px) scale(0.98);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }}
    
    .navbar-link.active {{
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
        border-color: rgba(255, 255, 255, 0.4);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.4);
        border-bottom: 3px solid white;
        font-weight: 700;
        transform: translateY(-2px);
    }}
    
    /* Ripple effect on click */
    .navbar-link {{
        --ripple-x: 0;
        --ripple-y: 0;
    }}
    
    @keyframes ripple {{
        0% {{
            box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7);
        }}
        70% {{
            box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
        }}
        100% {{
            box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
        }}
    }}
    
    .navbar-link:active {{
        animation: ripple 0.6s ease-out;
    }}
    
    @media (max-width: 768px) {{
        .navbar-container {{
            padding: 12px clamp(0.8rem, 3vw, 1.5rem);
            gap: clamp(0.4rem, 1vw, 0.6rem);
        }}
        
        .navbar-brand {{
            font-size: clamp(1rem, 2.5vw, 1.2rem);
            gap: 0.5rem;
        }}
        
        .navbar-link {{
            padding: clamp(0.55rem, 1vw, 0.7rem) clamp(0.5rem, 1vw, 0.9rem);
            font-size: clamp(0.7rem, 1.5vw, 0.85rem);
            border-radius: 6px;
        }}
        
        .navbar-link:hover {{
            transform: translateY(-2px) scale(1.01);
        }}
    }}
    
    @media (max-width: 480px) {{
        .navbar-container {{
            padding: 10px clamp(0.6rem, 2vw, 1rem);
            gap: 0.3rem;
        }}
        
        .navbar-brand {{
            font-size: clamp(0.95rem, 2vw, 1.1rem);
            gap: 0.4rem;
        }}
        
        .navbar-link {{
            padding: clamp(0.5rem, 0.8vw, 0.6rem) clamp(0.4rem, 0.8vw, 0.7rem);
            font-size: clamp(0.65rem, 1.2vw, 0.75rem);
            border-radius: 5px;
        }}
        
        .navbar-link:hover {{
            transform: translateY(-2px) scale(1.01);
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