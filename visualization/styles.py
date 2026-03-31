"""
CSS Styling for the application - Modern & Advanced Design
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
    Get complete CSS styling for the application with modern design.
    
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
    --transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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

/* ── Animated Background ── */
@keyframes gradientShift {{
    0%, 100% {{
        background-position: 0% 50%;
    }}
    50% {{
        background-position: 100% 50%;
    }}
}}

@keyframes floatUp {{
    0% {{
        opacity: 0;
        transform: translateY(20px);
    }}
    100% {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

@keyframes slideInLeft {{
    0% {{
        opacity: 0;
        transform: translateX(-30px);
    }}
    100% {{
        opacity: 1;
        transform: translateX(0);
    }}
}}

@keyframes glow {{
    0%, 100% {{
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
    }}
    50% {{
        box-shadow: 0 0 40px rgba(99, 102, 241, 0.6);
    }}
}}

@keyframes pulse {{
    0%, 100% {{
        opacity: 1;
    }}
    50% {{
        opacity: 0.7;
    }}
}}

/* ── Hero Section ── */
.hero {{
    background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, #a855f7 50%, {SECONDARY_COLOR} 100%);
    background-size: 200% 200%;
    border-radius: 24px;
    padding: clamp(2.5rem, 6vw, 4.5rem) clamp(2rem, 5vw, 4rem);
    margin-bottom: clamp(2rem, 5vw, 3.5rem);
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 25px 50px rgba(99, 102, 241, 0.3);
    animation: floatUp 0.8s ease-out;
    border: 1px solid rgba(255, 255, 255, 0.15);
}}

.hero::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 70% 30%, rgba(255,255,255,0.25) 0%, transparent 65%),
                radial-gradient(ellipse at 20% 80%, rgba(255,255,255,0.15) 0%, transparent 60%);
    pointer-events: none;
}}

.hero::after {{
    content: "";
    position: absolute;
    inset: -50%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: pulse 4s ease-in-out infinite;
    pointer-events: none;
}}

.hero-badge {{
    display: inline-block;
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(12px);
    border: 1.5px solid rgba(255,255,255,0.35);
    border-radius: 100px;
    padding: 0.6rem 1.5rem;
    font-size: clamp(0.65rem, 2vw, 0.8rem);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 1.2rem;
    font-weight: 700;
    animation: slideInLeft 0.8s ease-out;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}}

.hero h1 {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(2rem, 6vw, 3.8rem);
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 1rem;
    line-height: 1.1;
    letter-spacing: -1.2px;
    animation: floatUp 0.9s ease-out 0.1s both;
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}}

.hero p {{
    color: rgba(255,255,255,0.95);
    font-size: clamp(1rem, 2.8vw, 1.2rem);
    font-weight: 400;
    line-height: 1.7;
    letter-spacing: 0.4px;
    animation: floatUp 0.9s ease-out 0.2s both;
    max-width: 600px;
    margin: 0 auto;
}}

/* ── Section Headings ── */
.section-label {{
    font-size: clamp(0.65rem, 1.8vw, 0.8rem);
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 0.7rem;
    display: block;
    animation: slideInLeft 0.6s ease-out;
    text-shadow: 0 2px 4px rgba(99, 102, 241, 0.2);
}}

.section-title {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(1.6rem, 4.5vw, 2.5rem);
    font-weight: 900;
    color: var(--dark);
    margin-bottom: clamp(1.2rem, 3vw, 1.8rem);
    letter-spacing: -0.7px;
    animation: floatUp 0.7s ease-out;
    position: relative;
    display: inline-block;
}}

.section-title::after {{
    content: "";
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 2px;
    animation: floatUp 0.8s ease-out 0.2s both;
}}

/* ── Theory cards ── */
.theory-card {{
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1.5px solid var(--border);
    border-radius: 20px;
    padding: clamp(1.4rem, 3.5vw, 2rem);
    min-height: auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.07);
    transition: var(--transition);
    backdrop-filter: blur(10px);
    animation: floatUp 0.7s ease-out;
    position: relative;
    overflow: hidden;
}}

.theory-card::before {{
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.1), transparent);
    transition: left 0.6s ease;
}}

.theory-card:hover {{
    border-color: var(--primary);
    box-shadow: 0 15px 40px rgba(99, 102, 241, 0.2);
    transform: translateY(-8px) scale(1.01);
    background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%);
}}

.theory-card:hover::before {{
    left: 100%;
}}

.theory-card h4 {{
    color: var(--primary);
    font-size: clamp(1.05rem, 2.5vw, 1.3rem);
    font-weight: 800;
    margin: 0 0 1rem;
    letter-spacing: -0.4px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

.theory-card p, .theory-card li {{
    color: var(--text);
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.8;
    font-weight: 400;
}}

/* ── Pill badges ── */
.pill-row {{
    display: flex;
    gap: clamp(0.6rem, 2vw, 1rem);
    flex-wrap: wrap;
    margin-top: 1.2rem;
    justify-content: center;
}}

.pill {{
    background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%);
    border: 2px solid var(--primary-light);
    border-radius: 12px;
    padding: 0.7rem clamp(1rem, 2.5vw, 1.5rem);
    font-size: clamp(0.8rem, 1.8vw, 0.95rem);
    color: var(--primary);
    font-weight: 700;
    transition: var(--transition-smooth);
    cursor: pointer;
    position: relative;
    overflow: hidden;
}}

.pill::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    opacity: 0;
    transition: opacity 0.4s ease;
    z-index: -1;
}}

.pill:hover {{
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-color: transparent;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
    transform: translateY(-3px) scale(1.05);
}}

/* ── Input panels ── */
.input-panel {{
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 2px solid var(--border);
    border-radius: 18px;
    padding: clamp(1.2rem, 3vw, 1.8rem);
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: var(--transition-smooth);
    animation: floatUp 0.7s ease-out;
}}

.input-panel:hover {{
    border-color: var(--primary);
    box-shadow: 0 10px 30px rgba(99, 102, 241, 0.1);
}}

/* ── Metric Cards ── */
.metric-card {{
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 2px solid var(--border);
    border-radius: 20px;
    padding: clamp(1.4rem, 3.5vw, 2rem);
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    transition: var(--transition);
    animation: floatUp 0.7s ease-out;
    position: relative;
    overflow: hidden;
}}

.metric-card::after {{
    content: "";
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
    pointer-events: none;
}}

.metric-card:hover {{
    border-color: var(--primary);
    box-shadow: 0 15px 40px rgba(99, 102, 241, 0.15);
    transform: translateY(-6px) scale(1.02);
    background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%);
}}

.metric-card .label {{
    font-size: clamp(0.65rem, 1.8vw, 0.8rem);
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 0.8rem;
    display: block;
}}

.metric-card .value {{
    font-family: {FONT_SPACE_GROTESK};
    font-size: clamp(2rem, 6vw, 2.8rem);
    font-weight: 900;
    color: var(--primary);
    line-height: 1;
    letter-spacing: -1.2px;
    margin-top: 0.5rem;
    text-shadow: 0 2px 4px rgba(99, 102, 241, 0.1);
}}

/* ── Verdict Cards ── */
.verdict-reject {{
    background: linear-gradient(135deg, #fef2f2 0%, #fee8e8 100%);
    border: 2px solid #fca5a5;
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.8rem) clamp(1.2rem, 3vw, 2.2rem);
    color: #7f1d1d;
    font-weight: 600;
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    line-height: 1.8;
    animation: floatUp 0.7s ease-out;
    box-shadow: 0 8px 20px rgba(252, 165, 165, 0.15);
    position: relative;
    overflow: hidden;
}}

.verdict-reject::before {{
    content: "✕";
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 2.5rem;
    opacity: 0.1;
}}

.verdict-accept {{
    background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%);
    border: 2px solid #86efac;
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.8rem) clamp(1.2rem, 3vw, 2.2rem);
    color: #15803d;
    font-weight: 600;
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    line-height: 1.8;
    animation: floatUp 0.7s ease-out;
    box-shadow: 0 8px 20px rgba(134, 239, 172, 0.15);
    position: relative;
    overflow: hidden;
}}

.verdict-accept::before {{
    content: "✓";
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 2.5rem;
    opacity: 0.1;
}}

.insight-card {{
    background: linear-gradient(135deg, #fffbeb 0%, #fef9e7 100%);
    border: 2px solid #fcd34d;
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.8rem) clamp(1.2rem, 3vw, 2.2rem);
    color: #654321;
    line-height: 1.9;
    font-size: clamp(0.95rem, 2vw, 1.05rem);
    animation: floatUp 0.7s ease-out;
    box-shadow: 0 8px 20px rgba(252, 212, 77, 0.15);
    position: relative;
    overflow: hidden;
}}

.insight-card::before {{
    content: "💡";
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 2.5rem;
    opacity: 0.15;
}}

/* ── Divider ── */
.divider {{
    border: none;
    border-top: 2px solid var(--border);
    margin: clamp(2.5rem, 6vw, 3.5rem) 0;
    position: relative;
}}

.divider::after {{
    content: "";
    position: absolute;
    top: -1px;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 2px;
}}

/* ── Group Tiles ── */
.group-tile {{
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.2rem, 2.5vw, 1.5rem);
    font-size: clamp(0.85rem, 1.8vw, 1rem);
    color: var(--text);
    line-height: 1.9;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: var(--transition);
    animation: floatUp 0.7s ease-out;
}}

.group-tile:hover {{
    border-color: var(--primary);
    box-shadow: 0 12px 30px rgba(99, 102, 241, 0.15);
    transform: translateY(-4px);
    background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%);
}}

.group-tile strong {{
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    color: var(--primary);
    display: block;
    margin-bottom: 0.7rem;
    font-weight: 800;
}}

/* ── Button Override ── */
div.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    background-size: 200% 200%;
    color: white;
    border: none;
    border-radius: 14px;
    font-weight: 800;
    font-size: clamp(0.9rem, 1.8vw, 1.05rem);
    padding: clamp(0.7rem, 1.5vw, 0.95rem) clamp(1.2rem, 2.5vw, 2rem);
    letter-spacing: 0.5px;
    transition: var(--transition-smooth);
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.35);
    font-family: {FONT_POPPINS};
    position: relative;
    overflow: hidden;
}}

div.stButton > button[kind="primary"]::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, var(--secondary), var(--primary));
    opacity: 0;
    transition: opacity 0.4s ease;
}}

div.stButton > button[kind="primary"]:hover {{
    opacity: 0.95;
    box-shadow: 0 12px 30px rgba(99, 102, 241, 0.45);
    transform: translateY(-4px) scale(1.02);
}}

div.stButton > button[kind="primary"]:active {{
    transform: translateY(-2px) scale(0.98);
}}

/* ── Table Styling ── */
.table-wrapper {{
    background: #ffffff;
    border: 2px solid var(--border);
    border-radius: 18px;
    padding: clamp(1.2rem, 2.5vw, 1.8rem);
    overflow-x: auto;
    margin: clamp(1.5rem, 2vw, 2rem) 0;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    animation: floatUp 0.7s ease-out;
}}

.stats-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: clamp(0.8rem, 1.8vw, 0.95rem);
    background: white;
}}

.stats-table thead {{
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%);
}}

.stats-table th {{
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%) !important;
    color: var(--primary) !important;
    font-weight: 800 !important;
    padding: clamp(0.9rem, 1.8vw, 1.2rem) !important;
    text-align: center !important;
    border-bottom: 2.5px solid var(--primary) !important;
    font-size: clamp(0.75rem, 1.5vw, 0.9rem) !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
}}

.stats-table td {{
    padding: clamp(0.7rem, 1.5vw, 0.95rem) clamp(0.6rem, 1.2vw, 1.2rem) !important;
    border-bottom: 1.5px solid var(--border) !important;
    color: var(--text) !important;
    text-align: center !important;
    font-weight: 500;
}}

.stats-table tbody tr {{
    transition: var(--transition-smooth);
}}

.stats-table tbody tr:nth-child(odd) {{
    background: #f9fafb;
}}

.stats-table tbody tr:nth-child(even) {{
    background: #ffffff;
}}

.stats-table tbody tr:hover {{
    background: #f0f4ff !important;
    box-shadow: inset 0 0 8px rgba(99, 102, 241, 0.12);
}}

.stats-table tbody tr:hover td {{
    color: var(--primary) !important;
    font-weight: 700;
}}

/* ── Loading Animation ── */
@keyframes spinnerRotate {{
    from {{
        transform: rotate(0deg);
    }}
    to {{
        transform: rotate(360deg);
    }}
}}

.spinner {{
    animation: spinnerRotate 1.5s linear infinite;
}}

/* ── Mobile Responsive ── */
@media (max-width: 768px) {{
    .hero {{
        padding: 2.2rem 1.8rem;
        margin-bottom: 2.2rem;
        border-radius: 20px;
    }}
    
    .hero h1 {{
        font-size: 1.9rem;
        margin-bottom: 0.6rem;
    }}
    
    .hero p {{
        font-size: 1rem;
        line-height: 1.6;
    }}
    
    .hero-badge {{
        font-size: 0.7rem;
        padding: 0.5rem 1.2rem;
        margin-bottom: 1rem;
    }}
    
    .section-title {{
        font-size: 1.6rem;
        margin-bottom: 1.2rem;
    }}
    
    .section-label {{
        font-size: 0.7rem;
        margin-bottom: 0.4rem;
    }}
    
    .theory-card {{
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-radius: 16px;
    }}
    
    .theory-card h4 {{
        font-size: 1.05rem;
        margin-bottom: 0.7rem;
    }}
    
    .metric-card {{
        padding: 1.2rem;
        margin-bottom: 0.9rem;
        border-radius: 16px;
    }}
    
    .metric-card .value {{
        font-size: 1.9rem;
        margin-top: 0.4rem;
    }}
    
    .metric-card .label {{
        font-size: 0.7rem;
        margin-bottom: 0.4rem;
    }}
    
    .pill-row {{
        gap: 0.6rem;
        margin-top: 0.9rem;
    }}
    
    .pill {{
        padding: 0.6rem 1rem;
        font-size: 0.8rem;
        border-radius: 10px;
    }}
    
    .divider {{
        margin: 1.8rem 0;
    }}
    
    .verdict-reject,
    .verdict-accept,
    .insight-card {{
        padding: 1.1rem 1.4rem;
        font-size: 0.95rem;
        margin-bottom: 1.1rem;
        border-radius: 14px;
    }}
    
    .group-tile {{
        padding: 1.1rem;
        margin-bottom: 0.8rem;
        font-size: 0.9rem;
        border-radius: 14px;
    }}
    
    .group-tile strong {{
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }}
    
    .stats-table {{
        font-size: 0.8rem;
        overflow-x: auto;
    }}
    
    .stats-table th {{
        padding: 0.7rem 0.5rem !important;
        font-size: 0.7rem !important;
    }}
    
    .stats-table td {{
        padding: 0.6rem 0.4rem !important;
        font-size: 0.8rem !important;
    }}
    
    div.stButton > button[kind="primary"] {{
        width: 100%;
        font-size: 0.95rem;
        padding: 0.7rem 1rem;
        border-radius: 12px;
    }}
    
    .input-panel {{
        padding: 1.1rem;
        margin-bottom: 1.1rem;
        border-radius: 16px;
    }}
}}

@media (max-width: 480px) {{
    .hero {{
        padding: 1.6rem 1.2rem;
        border-radius: 18px;
        margin-bottom: 1.6rem;
    }}
    
    .hero h1 {{
        font-size: 1.4rem;
        margin-bottom: 0.5rem;
    }}
    
    .hero p {{
        font-size: 0.9rem;
        line-height: 1.6;
    }}
    
    .hero-badge {{
        font-size: 0.65rem;
        padding: 0.4rem 1rem;
        margin-bottom: 0.8rem;
    }}
    
    .section-title {{
        font-size: 1.3rem;
        margin-bottom: 0.9rem;
    }}
    
    .section-label {{
        font-size: 0.65rem;
        margin-bottom: 0.3rem;
    }}
    
    .theory-card {{
        padding: 1rem;
        margin-bottom: 0.9rem;
        border-radius: 14px;
    }}
    
    .theory-card h4 {{
        font-size: 0.95rem;
        margin-bottom: 0.6rem;
    }}
    
    .theory-card p {{
        font-size: 0.85rem;
        line-height: 1.7;
    }}
    
    .metric-card {{
        padding: 1rem;
        margin-bottom: 0.7rem;
        border-radius: 14px;
    }}
    
    .metric-card .value {{
        font-size: 1.6rem;
        margin-top: 0.3rem;
    }}
    
    .metric-card .label {{
        font-size: 0.65rem;
        margin-bottom: 0.3rem;
    }}
    
    .pill-row {{
        gap: 0.5rem;
        margin-top: 0.7rem;
    }}
    
    .pill {{
        padding: 0.5rem 0.9rem;
        font-size: 0.75rem;
        border-radius: 10px;
    }}
    
    .divider {{
        margin: 1.4rem 0;
    }}
    
    .verdict-reject,
    .verdict-accept,
    .insight-card {{
        padding: 1rem 1.2rem;
        font-size: 0.9rem;
        margin-bottom: 0.9rem;
        border-radius: 12px;
        border-width: 2px;
    }}
    
    .group-tile {{
        padding: 1rem;
        margin-bottom: 0.7rem;
        font-size: 0.85rem;
        border-radius: 12px;
    }}
    
    .group-tile strong {{
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
    }}
    
    .stats-table {{
        font-size: 0.75rem;
        width: 100%;
    }}
    
    .stats-table th {{
        padding: 0.6rem 0.3rem !important;
        font-size: 0.65rem !important;
        border-radius: 4px;
    }}
    
    .stats-table td {{
        padding: 0.5rem 0.25rem !important;
        font-size: 0.75rem !important;
    }}
    
    div.stButton > button[kind="primary"] {{
        width: 100%;
        font-size: 0.9rem;
        padding: 0.65rem 0.9rem;
        border-radius: 11px;
        font-weight: 700;
    }}
    
    .input-panel {{
        padding: 1rem;
        margin-bottom: 0.9rem;
        border-radius: 14px;
    }}
}}

/* ── Extra Small Devices (320px - 380px) ── */
@media (max-width: 380px) {{
    .hero {{
        padding: 1.3rem 1rem;
        border-radius: 16px;
    }}
    
    .hero h1 {{
        font-size: 1.2rem;
        margin-bottom: 0.4rem;
    }}
    
    .hero p {{
        font-size: 0.85rem;
    }}
    
    .section-title {{
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }}
    
    .metric-card {{
        padding: 0.9rem;
        margin-bottom: 0.6rem;
    }}
    
    .metric-card .value {{
        font-size: 1.4rem;
    }}
    
    .theory-card {{
        padding: 0.9rem;
        margin-bottom: 0.8rem;
    }}
    
    .theory-card h4 {{
        font-size: 0.9rem;
    }}
    
    div.stButton > button[kind="primary"] {{
        font-size: 0.85rem;
        padding: 0.6rem 0.8rem;
    }}
}}

/* ── Landscape Mode Adjustments ── */
@media (max-width: 768px) and (orientation: landscape) {{
    .hero {{
        padding: 1.5rem 1.2rem;
        margin-bottom: 1rem;
    }}
    
    .hero h1 {{
        font-size: 1.5rem;
    }}
    
    .section-title {{
        margin-bottom: 0.9rem;
        font-size: 1.3rem;
    }}
    
    .divider {{
        margin: 1.2rem 0;
    }}
}}

/* ── Scrollbar ── */
::-webkit-scrollbar {{
    width: 10px;
    height: 10px;
}}

::-webkit-scrollbar-track {{
    background: linear-gradient(180deg, #f1f5f9 0%, #e9ecef 100%);
    border-radius: 10px;
}}

::-webkit-scrollbar-thumb {{
    background: linear-gradient(180deg, var(--primary) 0%, var(--secondary) 100%);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(99, 102, 241, 0.2);
}}

::-webkit-scrollbar-thumb:hover {{
    background: linear-gradient(180deg, var(--primary-dark) 0%, var(--primary) 100%);
}}

/* ── Smooth Transitions ── */
input, textarea, select {{
    transition: var(--transition-smooth);
}}

input:focus, textarea:focus, select:focus {{
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
}}
</style>
"""
    return css