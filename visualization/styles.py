"""
CSS Styling for the application
"""

from config import (
    FONT_POPPINS,
    FONT_SPACE_GROTESK,
    PRIMARY_COLOR,
    PRIMARY_DARK,
    PRIMARY_LIGHT,
    SECONDARY_COLOR,
    SUCCESS_COLOR,
    DANGER_COLOR,
    DARK_COLOR,
    LIGHT_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
)


def get_css_styling():
    """
    Get complete CSS styling for the application.
    
    Returns:
        str: Complete CSS code as string
    """
    css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {{
    --primary: {PRIMARY_COLOR};
    --primary-dark: {PRIMARY_DARK};
    --primary-light: {PRIMARY_LIGHT};
    --secondary: {SECONDARY_COLOR};
    --success: {SUCCESS_COLOR};
    --danger: {DANGER_COLOR};
    --dark: {DARK_COLOR};
    --light: {LIGHT_COLOR};
    --border: {BORDER_COLOR};
    --text: {TEXT_COLOR};
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html, body, [class*="css"] {{
    font-family: {FONT_POPPINS};
    color: var(--dark);
    background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
}}

/* ── Hero Section ── */
.hero {{
    background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, #a855f7 50%, {SECONDARY_COLOR} 100%);
    border-radius: 20px;
    padding: clamp(2rem, 5vw, 4rem) clamp(1.5rem, 4vw, 3.5rem);
    margin-bottom: clamp(1.5rem, 4vw, 3rem);
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(99, 102, 241, 0.25);
}}

.hero::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 70% 30%, rgba(255,255,255,0.2) 0%, transparent 65%),
                radial-gradient(ellipse at 20% 80%, rgba(255,255,255,0.1) 0%, transparent 60%);
}}

.hero-badge {{
    display: inline-block;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 100px;
    padding: 0.5rem 1.2rem;
    font-size: clamp(0.65rem, 2vw, 0.75rem);
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 1rem;
    font-weight: 600;
}}

.hero h1 {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(1.8rem, 5vw, 3.5rem);
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 0.8rem;
    line-height: 1.1;
    letter-spacing: -1px;
}}

.hero p {{
    color: rgba(255,255,255,0.9);
    font-size: clamp(0.9rem, 2.5vw, 1.1rem);
    font-weight: 400;
    line-height: 1.6;
    letter-spacing: 0.3px;
}}

/* ── Section Headings ── */
.section-label {{
    font-size: clamp(0.6rem, 1.5vw, 0.75rem);
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 0.5rem;
    display: block;
}}

.section-title {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(1.5rem, 4vw, 2.2rem);
    font-weight: 700;
    color: var(--dark);
    margin-bottom: clamp(1rem, 3vw, 1.5rem);
    letter-spacing: -0.5px;
}}

/* ── Theory cards ── */
.theory-card {{
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.75rem);
    min-height: auto;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(10px);
}}

.theory-card:hover {{
    border-color: var(--primary);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
    transform: translateY(-4px);
}}

.theory-card h4 {{
    color: var(--primary);
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    font-weight: 700;
    margin: 0 0 0.8rem;
    letter-spacing: -0.3px;
}}

.theory-card p, .theory-card li {{
    color: var(--text);
    font-size: clamp(0.85rem, 1.8vw, 0.95rem);
    line-height: 1.7;
}}

/* ── Pill badges ── */
.pill-row {{
    display: flex;
    gap: clamp(0.5rem, 2vw, 0.75rem);
    flex-wrap: wrap;
    margin-top: 1rem;
    justify-content: center;
}}

.pill {{
    background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%);
    border: 1.5px solid var(--primary-light);
    border-radius: 8px;
    padding: 0.6rem clamp(0.8rem, 2vw, 1.2rem);
    font-size: clamp(0.75rem, 1.5vw, 0.85rem);
    color: var(--primary);
    font-weight: 600;
    transition: all 0.3s ease;
}}

.pill:hover {{
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-color: transparent;
}}

/* ── Input panels ── */
.input-panel {{
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: clamp(1rem, 3vw, 1.5rem);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}

/* ── Metric Cards ── */
.metric-card {{
    background: #ffffff;
    border: 2px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.5rem);
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}}

.metric-card:hover {{
    border-color: var(--primary);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12);
    transform: translateY(-2px);
}}

.metric-card .label {{
    font-size: clamp(0.6rem, 1.5vw, 0.7rem);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 0.5rem;
}}

.metric-card .value {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(1.8rem, 5vw, 2.2rem);
    font-weight: 800;
    color: var(--primary);
    line-height: 1;
    letter-spacing: -1px;
}}

/* ── Verdict Cards ── */
.verdict-reject {{
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
    border: 1.5px solid #fca5a5;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #991b1b;
    font-weight: 500;
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.6;
}}

.verdict-accept {{
    background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
    border: 1.5px solid #86efac;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #166534;
    font-weight: 500;
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.6;
}}

.insight-card {{
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 1.5px solid #fcd34d;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #78350f;
    line-height: 1.8;
    font-size: clamp(0.9rem, 2vw, 0.95rem);
}}

/* ── Divider ── */
.divider {{
    border: none;
    border-top: 1px solid var(--border);
    margin: clamp(2rem, 5vw, 3rem) 0;
}}

/* ── Group Tiles ── */
.group-tile {{
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1.5px solid var(--border);
    border-radius: 12px;
    padding: clamp(1rem, 2vw, 1.25rem);
    font-size: clamp(0.8rem, 1.5vw, 0.9rem);
    color: var(--text);
    line-height: 1.8;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}}

.group-tile:hover {{
    border-color: var(--primary);
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.1);
    transform: translateY(-2px);
}}

.group-tile strong {{
    font-size: clamp(0.9rem, 2vw, 1rem);
    color: var(--dark);
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 700;
}}

/* ── Button Override ── */
div.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    font-size: clamp(0.85rem, 1.5vw, 0.95rem);
    padding: clamp(0.6rem, 1.5vw, 0.8rem) clamp(1rem, 2vw, 1.75rem);
    letter-spacing: 0.3px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3);
    font-family: {FONT_POPPINS};
}}

div.stButton > button[kind="primary"]:hover {{
    opacity: 0.95;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
    transform: translateY(-2px);
}}

/* ── Table Styling ── */
.table-wrapper {{
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 12px;
    padding: clamp(1rem, 2vw, 1.5rem);
    overflow-x: auto;
    margin: clamp(1rem, 2vw, 1.5rem) 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}}

.stats-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: clamp(0.75rem, 1.5vw, 0.9rem);
    background: white;
}}

.stats-table thead {{
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%);
}}

.stats-table th {{
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%) !important;
    color: var(--dark) !important;
    font-weight: 700 !important;
    padding: clamp(0.75rem, 1.5vw, 1rem) !important;
    text-align: center !important;
    border-bottom: 2px solid var(--primary) !important;
    font-size: clamp(0.7rem, 1.3vw, 0.85rem) !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}}

.stats-table td {{
    padding: clamp(0.6rem, 1.5vw, 0.8rem) clamp(0.5rem, 1vw, 1rem) !important;
    border-bottom: 1px solid var(--border) !important;
    color: var(--text) !important;
    text-align: center !important;
}}

.stats-table tbody tr {{
    transition: all 0.3s ease;
}}

.stats-table tbody tr:nth-child(odd) {{
    background: #f9fafb;
}}

.stats-table tbody tr:nth-child(even) {{
    background: #ffffff;
}}

.stats-table tbody tr:hover {{
    background: #f0f4ff !important;
    box-shadow: inset 0 0 4px rgba(99, 102, 241, 0.1);
}}

.stats-table tbody tr:hover td {{
    color: var(--primary) !important;
    font-weight: 600;
}}

/* ── Mobile Responsive ── */
@media (max-width: 768px) {{
    .hero {{
        padding: 2rem 1.5rem;
        margin-bottom: 2rem;
        border-radius: 18px;
    }}
    
    .hero h1 {{
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }}
    
    .hero p {{
        font-size: 0.95rem;
    }}
    
    .hero-badge {{
        font-size: 0.65rem;
        padding: 0.4rem 1rem;
    }}
    
    .section-title {{
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }}
    
    .section-label {{
        font-size: 0.65rem;
        margin-bottom: 0.3rem;
    }}
    
    .theory-card {{
        padding: 1rem;
        margin-bottom: 1rem;
    }}
    
    .theory-card h4 {{
        font-size: 1rem;
        margin-bottom: 0.6rem;
    }}
    
    .metric-card {{
        padding: 1rem;
        margin-bottom: 0.75rem;
    }}
    
    .metric-card .value {{
        font-size: 1.8rem;
    }}
    
    .metric-card .label {{
        font-size: 0.65rem;
    }}
    
    .pill-row {{
        gap: 0.5rem;
        margin-top: 0.75rem;
    }}
    
    .pill {{
        padding: 0.5rem 0.8rem;
        font-size: 0.75rem;
    }}
    
    .divider {{
        margin: 1.5rem 0;
    }}
    
    .verdict-reject,
    .verdict-accept,
    .insight-card {{
        padding: 1rem 1.5rem;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        border-radius: 12px;
    }}
    
    .group-tile {{
        padding: 1rem;
        margin-bottom: 0.75rem;
        font-size: 0.85rem;
    }}
    
    .group-tile strong {{
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
    }}
    
    .stats-table {{
        font-size: 0.75rem;
        overflow-x: auto;
    }}
    
    .stats-table th {{
        padding: 0.6rem 0.4rem !important;
        font-size: 0.65rem !important;
    }}
    
    .stats-table td {{
        padding: 0.5rem 0.3rem !important;
    }}
    
    div.stButton > button[kind="primary"] {{
        width: 100%;
        font-size: 0.9rem;
        padding: 0.65rem 1rem;
    }}
    
    .input-panel {{
        padding: 1rem;
        margin-bottom: 1rem;
    }}
    
    [data-testid="stSidebar"] {{
        width: 280px !important;
    }}
}}

@media (max-width: 480px) {{
    .hero {{
        padding: 1.5rem 1rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
    }}
    
    .hero h1 {{
        font-size: 1.3rem;
        margin-bottom: 0.4rem;
    }}
    
    .hero p {{
        font-size: 0.85rem;
        line-height: 1.5;
    }}
    
    .hero-badge {{
        font-size: 0.6rem;
        padding: 0.3rem 0.8rem;
        margin-bottom: 0.8rem;
    }}
    
    .section-title {{
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }}
    
    .section-label {{
        font-size: 0.6rem;
        margin-bottom: 0.2rem;
    }}
    
    .theory-card {{
        padding: 0.9rem;
        margin-bottom: 0.8rem;
        border-radius: 12px;
    }}
    
    .theory-card h4 {{
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }}
    
    .theory-card p {{
        font-size: 0.8rem;
        line-height: 1.6;
    }}
    
    .metric-card {{
        padding: 0.9rem;
        margin-bottom: 0.6rem;
        border-radius: 12px;
    }}
    
    .metric-card .value {{
        font-size: 1.5rem;
        margin-top: 0.3rem;
    }}
    
    .metric-card .label {{
        font-size: 0.6rem;
        margin-bottom: 0.3rem;
    }}
    
    .pill-row {{
        gap: 0.4rem;
        margin-top: 0.6rem;
    }}
    
    .pill {{
        padding: 0.4rem 0.7rem;
        font-size: 0.7rem;
        border-radius: 6px;
    }}
    
    .divider {{
        margin: 1.2rem 0;
    }}
    
    .verdict-reject,
    .verdict-accept,
    .insight-card {{
        padding: 0.9rem 1.2rem;
        font-size: 0.85rem;
        margin-bottom: 0.8rem;
        border-radius: 10px;
        border-width: 1px;
    }}
    
    .group-tile {{
        padding: 0.85rem;
        margin-bottom: 0.6rem;
        font-size: 0.8rem;
        border-radius: 10px;
    }}
    
    .group-tile strong {{
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }}
    
    .stats-table {{
        font-size: 0.7rem;
        width: 100%;
    }}
    
    .stats-table th {{
        padding: 0.5rem 0.3rem !important;
        font-size: 0.6rem !important;
        border-radius: 4px;
    }}
    
    .stats-table td {{
        padding: 0.4rem 0.2rem !important;
    }}
    
    div.stButton > button[kind="primary"] {{
        width: 100%;
        font-size: 0.85rem;
        padding: 0.6rem 0.8rem;
        border-radius: 10px;
        font-weight: 600;
    }}
    
    .input-panel {{
        padding: 0.9rem;
        margin-bottom: 0.8rem;
        border-radius: 12px;
    }}
    
    [data-testid="stSidebar"] {{
        width: 250px !important;
    }}
    
    /* Stack columns vertically on very small screens */
    [data-testid="column"] {{
        display: block !important;
        width: 100% !important;
        margin-bottom: 1rem !important;
    }}
    
    .stContainer {{
        padding: 0.75rem !important;
    }}
    
    /* Ensure columns don't need side scrolling */
    [data-testid="stColumn"] {{
        min-width: 0 !important;
    }}
}}

/* ── Extra Small Devices (320px - 380px) ── */
@media (max-width: 380px) {{
    .hero {{
        padding: 1.2rem 0.8rem;
    }}
    
    .hero h1 {{
        font-size: 1.1rem;
    }}
    
    .hero p {{
        font-size: 0.8rem;
    }}
    
    .section-title {{
        font-size: 1.1rem;
        margin-bottom: 0.6rem;
    }}
    
    .metric-card {{
        padding: 0.8rem;
    }}
    
    .metric-card .value {{
        font-size: 1.3rem;
    }}
    
    .theory-card {{
        padding: 0.8rem;
    }}
    
    .theory-card h4 {{
        font-size: 0.85rem;
    }}
    
    div.stButton > button[kind="primary"] {{
        font-size: 0.8rem;
        padding: 0.55rem 0.7rem;
    }}
}}

/* ── Landscape Mode Adjustments ── */
@media (max-width: 768px) and (orientation: landscape) {{
    .hero {{
        padding: 1.5rem 1.2rem;
        margin-bottom: 1rem;
    }}
    
    .hero h1 {{
        font-size: 1.4rem;
    }}
    
    .section-title {{
        margin-bottom: 0.8rem;
        font-size: 1.2rem;
    }}
    
    .divider {{
        margin: 1rem 0;
    }}
}}

/* ── Scrollbar ── */
::-webkit-scrollbar {{
    width: 8px;
    height: 8px;
}}

::-webkit-scrollbar-track {{
    background: #f1f5f9;
}}

::-webkit-scrollbar-thumb {{
    background: var(--primary);
    border-radius: 4px;
}}

::-webkit-scrollbar-thumb:hover {{
    background: var(--primary-dark);
}}
</style>
"""
    return css
