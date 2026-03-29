"""
===============================================
📊 ANOVA Analysis Tool — Single-Page Streamlit App
===============================================
Run:
    pip install streamlit matplotlib seaborn scipy numpy
    streamlit run anova_app.py
===============================================
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
import base64
import io
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# ─── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="ANOVA Analysis Tool",
    page_icon="📊",
    layout="wide",
)

# ─── Global Style ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
    --secondary: #ec4899;
    --success: #10b981;
    --danger: #ef4444;
    --warning: #f59e0b;
    --info: #3b82f6;
    --dark: #1f2937;
    --light: #f9fafb;
    --border: #e5e7eb;
    --text: #4b5563;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, [class*="css"] {
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: var(--dark);
    background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
}

/* ── Hero Section ── */
.hero {
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
    border-radius: 20px;
    padding: clamp(2rem, 5vw, 4rem) clamp(1.5rem, 4vw, 3.5rem);
    margin-bottom: clamp(1.5rem, 4vw, 3rem);
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(99, 102, 241, 0.25);
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 70% 30%, rgba(255,255,255,0.2) 0%, transparent 65%),
                radial-gradient(ellipse at 20% 80%, rgba(255,255,255,0.1) 0%, transparent 60%);
}
.hero-badge {
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
}
.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.8rem, 5vw, 3.5rem);
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 0.8rem;
    line-height: 1.1;
    letter-spacing: -1px;
}
.hero p {
    color: rgba(255,255,255,0.9);
    font-size: clamp(0.9rem, 2.5vw, 1.1rem);
    font-weight: 400;
    line-height: 1.6;
    letter-spacing: 0.3px;
}

/* ── Section Headings ── */
.section-label {
    font-size: clamp(0.6rem, 1.5vw, 0.75rem);
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 0.5rem;
    display: block;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.5rem, 4vw, 2.2rem);
    font-weight: 700;
    color: var(--dark);
    margin-bottom: clamp(1rem, 3vw, 1.5rem);
    letter-spacing: -0.5px;
}

/* ── Theory cards ── */
.theory-card {
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.75rem);
    min-height: auto;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(10px);
}
.theory-card:hover {
    border-color: var(--primary);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
    transform: translateY(-4px);
}
.theory-card h4 {
    color: var(--primary);
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    font-weight: 700;
    margin: 0 0 0.8rem;
    letter-spacing: -0.3px;
}
.theory-card p, .theory-card li {
    color: var(--text);
    font-size: clamp(0.85rem, 1.8vw, 0.95rem);
    line-height: 1.7;
}

/* ── Pill badges ── */
.pill-row {
    display: flex;
    gap: clamp(0.5rem, 2vw, 0.75rem);
    flex-wrap: wrap;
    margin-top: 1rem;
    justify-content: center;
}
.pill {
    background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%);
    border: 1.5px solid var(--primary-light);
    border-radius: 8px;
    padding: 0.6rem clamp(0.8rem, 2vw, 1.2rem);
    font-size: clamp(0.75rem, 1.5vw, 0.85rem);
    color: var(--primary);
    font-weight: 600;
    transition: all 0.3s ease;
}
.pill:hover {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-color: transparent;
}

/* ── Input panels ── */
.input-panel {
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: clamp(1rem, 3vw, 1.5rem);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

/* ── Metric Cards ── */
.metric-card {
    background: #ffffff;
    border: 2px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.2rem, 3vw, 1.5rem);
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.metric-card:hover {
    border-color: var(--primary);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12);
    transform: translateY(-2px);
}
.metric-card .label {
    font-size: clamp(0.6rem, 1.5vw, 0.7rem);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 0.5rem;
}
.metric-card .value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.8rem, 5vw, 2.2rem);
    font-weight: 800;
    color: var(--primary);
    line-height: 1;
    letter-spacing: -1px;
}

/* ── Verdict Cards ── */
.verdict-reject {
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
    border: 1.5px solid #fca5a5;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #991b1b;
    font-weight: 500;
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.6;
}
.verdict-accept {
    background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
    border: 1.5px solid #86efac;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #166534;
    font-weight: 500;
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.6;
}
.insight-card {
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 1.5px solid #fcd34d;
    border-radius: 12px;
    padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 2rem);
    color: #78350f;
    line-height: 1.8;
    font-size: clamp(0.9rem, 2vw, 0.95rem);
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: clamp(2rem, 5vw, 3rem) 0;
}

/* ── Group Tiles ── */
.group-tile {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1.5px solid var(--border);
    border-radius: 12px;
    padding: clamp(1rem, 2vw, 1.25rem);
    font-size: clamp(0.8rem, 1.5vw, 0.9rem);
    color: var(--text);
    line-height: 1.8;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.group-tile:hover {
    border-color: var(--primary);
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.1);
    transform: translateY(-2px);
}
.group-tile strong {
    font-size: clamp(0.9rem, 2vw, 1rem);
    color: var(--dark);
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

/* ── Graph Description ── */
.graph-description {
    background: linear-gradient(135deg, #f9fafb 0%, #f0f4fb 100%);
    border-left: 4px solid var(--primary);
    border-radius: 8px;
    padding: clamp(0.75rem, 2vw, 1rem);
    margin-bottom: clamp(1rem, 2vw, 1.5rem);
    font-size: clamp(0.8rem, 1.5vw, 0.9rem);
    color: var(--text);
    line-height: 1.6;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

/* ── Button Override ── */
div.stButton > button[kind="primary"] {
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
    font-family: 'Poppins', sans-serif;
}
div.stButton > button[kind="primary"]:hover {
    opacity: 0.95;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
    transform: translateY(-2px);
}

/* ── Table Styling ── */
.table-wrapper {
    background: #ffffff;
    border: 1.5px solid var(--border);
    border-radius: 12px;
    padding: clamp(1rem, 2vw, 1.5rem);
    overflow-x: auto;
    margin: clamp(1rem, 2vw, 1.5rem) 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.stats-table {
    width: 100%;
    border-collapse: collapse;
    font-size: clamp(0.75rem, 1.5vw, 0.9rem);
    background: white;
}

.stats-table thead {
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%);
}

.stats-table th {
    background: linear-gradient(135deg, #f3f4f6 0%, #eef2ff 100%) !important;
    color: var(--dark) !important;
    font-weight: 700 !important;
    padding: clamp(0.75rem, 1.5vw, 1rem) !important;
    text-align: center !important;
    border-bottom: 2px solid var(--primary) !important;
    font-size: clamp(0.7rem, 1.3vw, 0.85rem) !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}

.stats-table td {
    padding: clamp(0.6rem, 1.5vw, 0.8rem) clamp(0.5rem, 1vw, 1rem) !important;
    border-bottom: 1px solid var(--border) !important;
    color: var(--text) !important;
    text-align: center !important;
}

.stats-table tbody tr {
    transition: all 0.3s ease;
}

.stats-table tbody tr:nth-child(odd) {
    background: #f9fafb;
}

.stats-table tbody tr:nth-child(even) {
    background: #ffffff;
}

.stats-table tbody tr:hover {
    background: #f0f4ff !important;
    box-shadow: inset 0 0 4px rgba(99, 102, 241, 0.1);
}

.stats-table tbody tr:hover td {
    color: var(--primary) !important;
    font-weight: 600;
}

/* ── Mobile Responsive ── */
@media (max-width: 768px) {
    .hero {
        padding: 2rem 1.5rem;
        margin-bottom: 2rem;
    }
    
    .hero h1 {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    
    .hero p {
        font-size: 0.95rem;
    }
    
    .section-title {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .pill-row {
        justify-content: flex-start;
        gap: 0.5rem;
    }
    
    .metric-card {
        padding: 1rem;
    }
    
    .metric-card .value {
        font-size: 1.8rem;
    }
    
    .stats-table {
        font-size: 0.75rem;
    }
    
    .stats-table th {
        padding: 0.6rem 0.4rem !important;
        font-size: 0.65rem !important;
    }
    
    .stats-table td {
        padding: 0.5rem 0.3rem !important;
    }
    
    .verdict-reject, .verdict-accept, .insight-card {
        padding: 1rem;
        font-size: 0.9rem;
    }
    
    .table-wrapper {
        padding: 1rem;
        margin: 1rem 0;
    }
}

@media (max-width: 480px) {
    .hero {
        padding: 1.5rem 1rem;
        border-radius: 16px;
    }
    
    .hero h1 {
        font-size: 1.5rem;
    }
    
    .hero p {
        font-size: 0.9rem;
    }
    
    .section-title {
        font-size: 1.3rem;
    }
    
    .theory-card {
        padding: 1rem;
    }
    
    .metric-card {
        padding: 0.8rem;
    }
    
    .metric-card .label {
        font-size: 0.55rem;
        letter-spacing: 1px;
    }
    
    .metric-card .value {
        font-size: 1.5rem;
        margin-top: 0.5rem;
    }
    
    .stats-table {
        font-size: 0.7rem;
    }
    
    .stats-table th {
        padding: 0.5rem 0.25rem !important;
        font-size: 0.6rem !important;
    }
    
    .stats-table td {
        padding: 0.4rem 0.2rem !important;
    }
    
    .group-tile {
        padding: 0.8rem;
        margin-bottom: 0.8rem;
    }
    
    div.stButton > button[kind="primary"] {
        font-size: 0.85rem;
        padding: 0.6rem 1rem;
        width: 100%;
    }
}

/* ── Scrollbar ── */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #f1f5f9;
}
::-webkit-scrollbar-thumb {
    background: var(--primary);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--primary-dark);
}
</style>
""", unsafe_allow_html=True)

# ─── Palette & Seaborn ─────────────────────────────────────────
sns.set_theme(style="white", palette="muted")
COLORS = ["#667eea", "#ef5350", "#66bb6a", "#ffa726", "#764ba2", "#26a69a"]

# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def parse_input(text: str):
    text = text.strip()
    if not text:
        return None
    try:
        values = [float(x.strip()) for x in text.split(",") if x.strip()]
        return values if len(values) >= 2 else None
    except ValueError:
        return None

def run_anova(*groups):
    return stats.f_oneway(*groups)

def generate_report(group_data, f_stat, p_value, alpha):
    lines = ["=" * 52, "  ANOVA Results Report", "=" * 52, ""]
    for name, data in group_data.items():
        arr = np.array(data)
        lines.append(f"  {name}:  n={len(arr)}, Mean={arr.mean():.4f}, Std={arr.std(ddof=1):.4f}")
    lines += ["", "-" * 52,
              f"  F-statistic : {f_stat:.4f}",
              f"  P-value     : {p_value:.6f}",
              f"  Alpha (α)   : {alpha}", "-" * 52, ""]
    if p_value < alpha:
        lines.append("  ✘ REJECT H₀ — Significant differences found.")
    else:
        lines.append("  ✔ FAIL TO REJECT H₀ — No significant difference.")
    means = {n: np.mean(d) for n, d in group_data.items()}
    best = max(means, key=means.get)
    lines += ["", f"  Highest mean: {best} ({means[best]:.4f})", "", "=" * 52]
    return "\n".join(lines)

def fig_to_base64(fig):
    """Convert matplotlib figure to base64 string"""
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    return image_base64

def generate_pdf_report(group_data, f_stat, p_value, alpha, eta_squared, levene_stat, levene_p, all_values, 
                       fig_box_bytes, fig_bar_bytes, fig_kde_bytes, fig_hist_bytes, fig_violin_bytes, 
                       fig_heatmap_bytes, fig_range_bytes):
    """Generate comprehensive PDF report with ALL statistics, tables, and visualizations"""
    if not PDF_AVAILABLE:
        return None
    
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
        from reportlab.lib import colors
        
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.4*inch, bottomMargin=0.4*inch)
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=22, 
                                     textColor=colors.HexColor('#667eea'), spaceAfter=6, alignment=1)
        heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=13,
                                       textColor=colors.HexColor('#667eea'), spaceAfter=10, spaceBefore=10)
        normal_style = ParagraphStyle('CustomNormal', parent=styles['Normal'], fontSize=9, spaceAfter=4)
        desc_style = ParagraphStyle('Desc', parent=styles['Normal'], fontSize=8, 
                                    textColor=colors.HexColor('#6b7280'), spaceAfter=8, leftIndent=10)
        
        # Title
        story.append(Paragraph("📊 ANOVA Analysis Report", title_style))
        story.append(Spacer(1, 0.15*inch))
        
        # ── Key Results ──
        story.append(Paragraph("Key Results", heading_style))
        rejected = p_value < alpha
        key_results = f"""<b>F-Statistic:</b> {f_stat:.4f} | <b>P-Value:</b> {p_value:.6f} | <b>α:</b> {alpha} | <b>η²:</b> {eta_squared:.4f}<br/>
        <b>Conclusion:</b> {'✘ REJECT H₀ — Significant difference' if rejected else '✔ FAIL TO REJECT H₀ — No difference'}"""
        story.append(Paragraph(key_results, normal_style))
        story.append(Spacer(1, 0.15*inch))
        
        # ── Descriptive Statistics Table ──
        story.append(Paragraph("Descriptive Statistics by Group", heading_style))
        table_data = [["Group", "N", "Mean", "Median", "Std Dev", "Min", "Max", "Q1", "Q3"]]
        for name, data in group_data.items():
            arr = np.array(data)
            table_data.append([
                name, str(len(arr)), f"{arr.mean():.3f}", f"{np.median(arr):.3f}",
                f"{arr.std(ddof=1):.3f}", f"{arr.min():.3f}", f"{arr.max():.3f}",
                f"{np.percentile(arr, 25):.3f}", f"{np.percentile(arr, 75):.3f}"
            ])
        
        table = Table(table_data, colWidths=[0.9*inch, 0.45*inch, 0.55*inch, 0.55*inch, 0.55*inch, 
                                             0.45*inch, 0.45*inch, 0.45*inch, 0.45*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f3f4f6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1f2937')),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9fafb')),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#4b5563')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e5e7eb')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')]),
        ]))
        story.append(table)
        story.append(Spacer(1, 0.15*inch))
        
        # ── Assumption Testing & Effect Size ──
        story.append(Paragraph("Assumption Testing & Effect Size", heading_style))
        assumption_text = f"""<b>Levene's Test:</b> {levene_stat:.4f} (p={levene_p:.4f}) — {'✅ Equal variances' if levene_p >= 0.05 else '⚠️ Unequal variances'}<br/>
        <b>Effect Size (η²):</b> {eta_squared:.4f} — {'Large' if eta_squared >= 0.14 else ('Medium' if eta_squared >= 0.06 else ('Small' if eta_squared >= 0.01 else 'Negligible'))} ({eta_squared*100:.2f}% variance explained)"""
        story.append(Paragraph(assumption_text, normal_style))
        story.append(Spacer(1, 0.15*inch))
        
        # ── ANOVA Summary Table ──
        story.append(Paragraph("ANOVA Summary Table", heading_style))
        grand_mean = np.mean(all_values)
        ss_between = sum(len(group_data[name]) * (np.mean(group_data[name]) - grand_mean)**2 for name in group_data)
        ss_within = sum(sum((val - np.mean(group_data[name]))**2 for val in group_data[name]) for name in group_data)
        ss_total = sum((val - grand_mean)**2 for val in all_values)
        df_between = len(group_data) - 1
        df_within = len(all_values) - len(group_data)
        ms_between = ss_between / max(df_between, 1)
        ms_within = ss_within / max(df_within, 1)
        
        anova_data = [
            ["Source", "Sum of Squares", "DF", "Mean Square", "F-Statistic", "P-Value"],
            ["Between", f"{ss_between:.3f}", str(df_between), f"{ms_between:.3f}", f"{f_stat:.4f}", f"{p_value:.6f}"],
            ["Within", f"{ss_within:.3f}", str(df_within), f"{ms_within:.3f}", "—", "—"],
            ["Total", f"{ss_total:.3f}", str(df_between + df_within), "—", "—", "—"]
        ]
        
        anova_table = Table(anova_data, colWidths=[1.0*inch, 1.3*inch, 0.6*inch, 1.0*inch, 1.0*inch, 1.0*inch])
        anova_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e5e7eb')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')]),
        ]))
        story.append(anova_table)
        story.append(Spacer(1, 0.2*inch))
        
        # ── Page Break before visualizations ──
        story.append(PageBreak())
        story.append(Paragraph("Visualizations & Analysis", heading_style))
        story.append(Spacer(1, 0.1*inch))
        
        # All visualizations
        viz_list = [
            ("Distribution by Group", fig_box_bytes, "Box plot shows median, quartiles, and outliers for each group."),
            ("Mean Comparison (± Std Dev)", fig_bar_bytes, "Bar chart displays group means with standard deviation error bars."),
            ("Density Distribution (KDE)", fig_kde_bytes, "Smooth kernel density curves show probability distribution."),
            ("Overlaid Histograms", fig_hist_bytes, "Frequency distribution for each group with overlapping ranges."),
            ("Violin Plot", fig_violin_bytes, "Combines box plot with density curve to show full distribution shape."),
            ("Summary Statistics Heatmap", fig_heatmap_bytes, "Color-coded matrix showing mean, std dev, and count for each group."),
            ("Range, IQR & Median", fig_range_bytes, "Full data range, interquartile range, and median position."),
        ]
        
        for title, fig_bytes, desc in viz_list:
            if fig_bytes:
                fig_bytes.seek(0)
                story.append(Paragraph(title, ParagraphStyle('VizTitle', parent=styles['Normal'], 
                                                             fontSize=10, textColor=colors.HexColor('#667eea'), 
                                                             fontName='Helvetica-Bold', spaceAfter=4)))
                story.append(Image(fig_bytes, width=5.5*inch, height=2.75*inch))
                story.append(Paragraph(f"<i>{desc}</i>", desc_style))
                story.append(Spacer(1, 0.15*inch))
        
        # Footer
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph(f"<i>Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>", 
                              ParagraphStyle('Footer', parent=styles['Normal'], fontSize=7, alignment=1)))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    
    except Exception as e:
        st.warning(f"PDF generation error: {str(e)}")
        return None

def generate_html_report(group_data, f_stat, p_value, alpha, all_values, eta_squared, levene_stat, levene_p):
    """Generate comprehensive HTML report with all tables and graphs"""
    import io
    
    rejected = p_value < alpha
    
    # Calculate statistics
    means_dict = {n: np.mean(d) for n, d in group_data.items()}
    best = max(means_dict, key=means_dict.get)
    worst = min(means_dict, key=means_dict.get)
    
    # Determine variance assumption result
    variance_result = '✅ Equal variances assumed (p ≥ 0.05)' if levene_p >= 0.05 else '⚠️ Variances may differ (p < 0.05)'
    
    # Start HTML with escaped braces for CSS
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ANOVA Analysis Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #1f2937;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f9fafb;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5rem;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .section {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .metric {{
            background: #f3f4f6;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border-left: 4px solid #667eea;
        }}
        .metric-label {{
            font-size: 0.85rem;
            color: #6b7280;
            text-transform: uppercase;
            font-weight: 600;
        }}
        .metric-value {{
            font-size: 1.8rem;
            color: #667eea;
            font-weight: 700;
            margin-top: 8px;
        }}
        .verdict {{
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            font-weight: 500;
        }}
        .verdict-reject {{
            background: #fef2f2;
            border-left: 4px solid #fca5a5;
            color: #991b1b;
        }}
        .verdict-accept {{
            background: #f0fdf4;
            border-left: 4px solid #86efac;
            color: #166534;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        thead {{
            background: #f3f4f6;
        }}
        th {{
            padding: 12px;
            text-align: left;
            font-weight: 700;
            color: #1f2937;
            border-bottom: 2px solid #667eea;
            font-size: 0.85rem;
            text-transform: uppercase;
        }}
        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #e5e7eb;
        }}
        tbody tr:nth-child(odd) {{
            background: #f9fafb;
        }}
        tbody tr:hover {{
            background: #f0f4ff;
        }}
        .graph {{
            text-align: center;
            margin: 20px 0;
        }}
        .graph img {{
            max-width: 100%;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .footer {{
            text-align: center;
            color: #6b7280;
            border-top: 1px solid #e5e7eb;
            padding-top: 20px;
            margin-top: 40px;
            font-size: 0.9rem;
        }}
        .insight {{
            background: #fffbeb;
            border-left: 4px solid #fcd34d;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            color: #78350f;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 ANOVA Analysis Report</h1>
        <p>Statistical Analysis of {len(group_data)} Groups</p>
        <p style="margin-top: 15px; font-size: 0.9rem;">Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

    <div class="section">
        <h2>🎯 Key Results</h2>
        <div class="metrics">
            <div class="metric">
                <div class="metric-label">F-Statistic</div>
                <div class="metric-value">{f_stat:.4f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">P-Value</div>
                <div class="metric-value">{p_value:.6f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Alpha (α)</div>
                <div class="metric-value">{alpha}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Effect Size (η²)</div>
                <div class="metric-value">{eta_squared:.4f}</div>
            </div>
        </div>
        {"<div class='verdict verdict-reject'><strong>✘ Reject H₀</strong> — Statistically significant difference detected (p < α)</div>" if rejected else "<div class='verdict verdict-accept'><strong>✔ Fail to Reject H₀</strong> — No significant difference (p ≥ α)</div>"}
    </div>

    <div class="section">
        <h2>📈 Descriptive Statistics by Group</h2>
        <table>
            <thead>
                <tr>
                    <th>Group</th>
                    <th>N</th>
                    <th>Mean</th>
                    <th>Median</th>
                    <th>Std Dev</th>
                    <th>Min</th>
                    <th>Max</th>
                    <th>Q1</th>
                    <th>Q3</th>
                </tr>
            </thead>
            <tbody>
"""
    
    for name, data in group_data.items():
        arr = np.array(data)
        html += f"""                <tr>
                    <td><strong>{name}</strong></td>
                    <td>{len(arr)}</td>
                    <td>{arr.mean():.4f}</td>
                    <td>{np.median(arr):.4f}</td>
                    <td>{arr.std(ddof=1):.4f}</td>
                    <td>{arr.min():.4f}</td>
                    <td>{arr.max():.4f}</td>
                    <td>{np.percentile(arr, 25):.4f}</td>
                    <td>{np.percentile(arr, 75):.4f}</td>
                </tr>
"""
    
    html += f"""            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>🔬 Assumption Testing</h2>
        <div class="metrics">
            <div class="metric">
                <div class="metric-label">Levene's Test</div>
                <div class="metric-value">{levene_stat:.4f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Levene's P-Value</div>
                <div class="metric-value">{levene_p:.4f}</div>
            </div>
        </div>
        <p><strong>Homogeneity of Variance:</strong> {variance_result}</p>
    </div>

    <div class="section">
        <h2>💡 Interpretation & Insights</h2>
"""
    
    if rejected:
        effect_size_text = 'Large' if eta_squared >= 0.14 else ('Medium' if eta_squared >= 0.06 else ('Small' if eta_squared >= 0.01 else 'Negligible'))
        html += f"""        <div class="insight">
            <strong>Significant Difference Detected</strong><br><br>
            🏆 <strong>{best}</strong> has the highest mean ({means_dict[best]:.4f})<br>
            📉 <strong>{worst}</strong> has the lowest mean ({means_dict[worst]:.4f})<br><br>
            Effect Size: {effect_size_text} ({eta_squared*100:.2f}% variance explained)<br><br>
            <strong>Recommendation:</strong> Conduct post-hoc tests (Tukey HSD, Bonferroni) to identify specific group differences.
        </div>
"""
    else:
        effect_size_text = 'Large' if eta_squared >= 0.14 else ('Medium' if eta_squared >= 0.06 else ('Small' if eta_squared >= 0.01 else 'Negligible'))
        html += f"""        <div class="insight">
            <strong>No Significant Difference</strong><br><br>
            While {best} has the highest mean ({means_dict[best]:.4f}) and {worst} the lowest ({means_dict[worst]:.4f}), 
            the difference is not statistically significant.<br><br>
            Effect Size: {effect_size_text} ({eta_squared*100:.2f}% variance explained)<br><br>
            <strong>Recommendation:</strong> Increase sample size if attempting to detect smaller differences.
        </div>
"""
    
    html += """    </div>

    <div class="footer">
        <p>ANOVA Analysis Tool | Statistical Analysis Report</p>
    </div>
</body>
</html>
"""
    
    return html

SAMPLE_DATASETS = {
    "Student Exam Scores (3 teaching methods)": {
        "Method A": [85, 90, 78, 92, 88, 76, 95, 89],
        "Method B": [70, 65, 72, 68, 74, 71, 69, 73],
        "Method C": [80, 82, 79, 85, 83, 81, 78, 84],
    },
    "Crop Yield (3 fertilizers)": {
        "Fertilizer X": [20, 22, 19, 24, 25, 21, 23],
        "Fertilizer Y": [28, 30, 27, 26, 29, 31, 32],
        "Fertilizer Z": [22, 23, 21, 20, 24, 22, 25],
    },
    "No Significant Difference (similar groups)": {
        "Group 1": [50, 52, 48, 51, 49, 53, 50],
        "Group 2": [51, 49, 50, 52, 48, 50, 51],
        "Group 3": [50, 51, 49, 52, 50, 48, 51],
    },
}

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div class="hero-badge">Statistical Analysis</div>
  <h1>ANOVA Analysis Tool</h1>
  <p>Compare means across three or more groups — instantly interpret variance, significance & insights.</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 1 — THEORY
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">01 — Background</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">What is ANOVA?</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="theory-card">
      <h4>📐 The Concept</h4>
      <p>ANOVA (<em>Analysis of Variance</em>) tests whether the means of <strong>3+ groups</strong>
      differ significantly — all in one test, avoiding the inflated error rate of multiple t-tests.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="theory-card">
      <h4>📊 The F-Statistic</h4>
      <p>ANOVA compares <strong>between-group variance</strong> to <strong>within-group variance</strong>:</p>
      <p style="margin-top:0.6rem; font-size:1rem; text-align:center; font-weight:600; color:#303f9f">
        F = Var(between) / Var(within)
      </p>
      <p>A large F signals the groups differ more than chance alone would predict.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="theory-card">
      <h4>🔬 Hypotheses</h4>
      <p><strong>H₀ (Null):</strong> All group means are equal — μ₁ = μ₂ = … = μₖ</p>
      <br>
      <p><strong>H₁ (Alternative):</strong> At least one group mean differs from the rest.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="margin-top:1rem"></div>', unsafe_allow_html=True)

st.markdown("""
<p style="font-size:0.8rem;font-weight:600;color:#7986cb;letter-spacing:2px;margin-bottom:0.5rem">
ASSUMPTIONS
</p>
<div class="pill-row">
  <span class="pill">✅ Independence of observations</span>
  <span class="pill">✅ Approximate normality per group</span>
  <span class="pill">✅ Homogeneity of variance</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 2 — SETTINGS + INPUT
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">02 — Configure</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Settings & Data Input</p>', unsafe_allow_html=True)

set_col1, set_col2, set_col3 = st.columns([1, 1, 2])
with set_col1:
    alpha = st.slider("Significance level (α)", 0.01, 0.10, 0.05, 0.01,
                      help="Threshold for rejecting H₀. Common choice: 0.05")
with set_col2:
    num_groups = st.slider("Number of groups", 2, 6, 3,
                           help="How many groups you want to compare")
with set_col3:
    sample_choice = st.selectbox(
        "⚡ Load a sample dataset",
        ["— Choose a sample —"] + list(SAMPLE_DATASETS.keys()),
        help="Auto-fills the group inputs below"
    )

# Load sample into session state
if sample_choice != "— Choose a sample —":
    sample = SAMPLE_DATASETS[sample_choice]
    sample_keys = list(sample.keys())
    for i in range(min(len(sample_keys), num_groups)):
        st.session_state[f"gn_{i}"] = sample_keys[i]
        st.session_state[f"gd_{i}"] = ", ".join(str(v) for v in sample[sample_keys[i]])

st.markdown('<div style="margin-top:1rem"></div>', unsafe_allow_html=True)

# Group inputs
group_data = {}
all_valid = True

cols = st.columns(min(num_groups, 3))
for i in range(num_groups):
    with cols[i % 3]:
        with st.container(border=True):
            default_name = st.session_state.get(f"gn_{i}", f"Group {i + 1}")
            default_data = st.session_state.get(f"gd_{i}", "")

            name = st.text_input(f"Group {i + 1} name", value=default_name, key=f"gn_{i}")
            raw = st.text_area("Values (comma-separated)", value=default_data,
                               key=f"gd_{i}", height=80,
                               placeholder="e.g. 85, 90, 78, 92")

            parsed = parse_input(raw)
            if raw.strip() and parsed is None:
                st.error("⚠️ Need ≥ 2 valid numbers.")
                all_valid = False
            elif parsed:
                group_data[name] = parsed
                arr = np.array(parsed)
                st.caption(f"n = {len(parsed)} · mean = {arr.mean():.2f} · std = {arr.std(ddof=1):.2f}")

st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)

btn_col, reset_col = st.columns([5, 1])
with btn_col:
    run_clicked = st.button("🚀 Run ANOVA Analysis", type="primary", use_container_width=True)
with reset_col:
    if st.button("🔄 Reset", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

if run_clicked:
    if len(group_data) < 2:
        st.error("Please provide valid data for at least 2 groups.")
    elif not all_valid:
        st.error("Please fix invalid inputs before running.")
    else:
        f_stat, p_value = run_anova(*group_data.values())
        st.session_state["anova_results"] = {
            "group_data": group_data,
            "f_stat": f_stat,
            "p_value": p_value,
            "alpha": alpha,
        }

# ═══════════════════════════════════════════════════════════════
# SECTION 3 — RESULTS
# ═══════════════════════════════════════════════════════════════
if "anova_results" in st.session_state:
    res = st.session_state["anova_results"]
    group_data = res["group_data"]
    f_stat = res["f_stat"]
    p_value = res["p_value"]
    a = res["alpha"]
    rejected = p_value < a

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">03 — Output</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Results</p>', unsafe_allow_html=True)

    # ── Key Metrics ──────────────────────────────────────────
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">F-Statistic</div>
          <div class="value">{f_stat:.4f}</div>
        </div>""", unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">P-Value</div>
          <div class="value">{p_value:.4f}</div>
        </div>""", unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Alpha (α)</div>
          <div class="value">{a}</div>
        </div>""", unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Groups</div>
          <div class="value">{len(group_data)}</div>
        </div>""", unsafe_allow_html=True)
    with m5:
        sig_text = "✔ YES" if rejected else "✘ NO"
        sig_color = "#16a34a" if rejected else "#dc2626"
        st.markdown(f"""
        <div class="metric-card" style="border-color: {sig_color}; background: linear-gradient(135deg, rgba({int(sig_color[1:3], 16)}, {int(sig_color[3:5], 16)}, {int(sig_color[5:7], 16)}, 0.05), rgba({int(sig_color[1:3], 16)}, {int(sig_color[3:5], 16)}, {int(sig_color[5:7], 16)}, 0.02));">
          <div class="label">Significant</div>
          <div class="value" style="color: {sig_color}; font-size: 1.8rem;">{sig_text}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div style="margin-top:1.25rem"></div>', unsafe_allow_html=True)

    # ── Verdict ──────────────────────────────────────────────
    if rejected:
        st.markdown(
            f'<div class="verdict-reject">'
            f'<strong>✘ Reject H₀</strong> — A statistically significant difference exists between '
            f'at least two group means (p = {p_value:.6f} &lt; α = {a}).'
            f'</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="verdict-accept">'
            f'<strong>✔ Fail to Reject H₀</strong> — No statistically significant difference '
            f'between group means (p = {p_value:.6f} ≥ α = {a}).'
            f'</div>', unsafe_allow_html=True)

    # ── Group Summary ─────────────────────────────────────────
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)
    st.markdown("**Group Summary**")
    tile_cols = st.columns(len(group_data))
    for idx, (name, data) in enumerate(group_data.items()):
        arr = np.array(data)
        color = COLORS[idx % len(COLORS)]
        with tile_cols[idx]:
            st.markdown(f"""
            <div class="group-tile" style="border-left: 4px solid {color};">
              <strong>{name}</strong>
              n = {len(arr)}<br>
              Mean = {arr.mean():.4f}<br>
              Std = {arr.std(ddof=1):.4f}<br>
              Range = [{arr.min()}, {arr.max()}]
            </div>""", unsafe_allow_html=True)

    # ── Visualizations ────────────────────────────────────────
    st.markdown('<div style="margin-top:2rem"></div>', unsafe_allow_html=True)
    st.markdown("## 📊 Visualizations & Analysis")

    all_values, all_labels = [], []
    for name, data in group_data.items():
        all_values.extend(data)
        all_labels.extend([name] * len(data))

    group_names = list(group_data.keys())
    group_means = [np.mean(v) for v in group_data.values()]
    group_stds  = [np.std(v, ddof=1) for v in group_data.values()]

    # ── Row 1: Boxplot, Bar Chart, KDE ──
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.patch.set_facecolor("#ffffff")

    ax_style = dict(facecolor="#ffffff", labelcolor="#455a64", titlecolor="#1a237e",
                    labelsize=9)

    # Boxplot
    ax = axes[0]
    bp = ax.boxplot(
        [group_data[g] for g in group_names],
        labels=group_names,
        patch_artist=True,
        widths=0.45,
        medianprops=dict(color="#667eea", linewidth=2.5),
        whiskerprops=dict(linewidth=1.2, color="#9ca3af"),
        capprops=dict(linewidth=1.5, color="#9ca3af"),
        flierprops=dict(marker="o", markersize=5, color="#d1d5db"),
    )
    for patch, color in zip(bp["boxes"], COLORS):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
        patch.set_edgecolor("#667eea")
        patch.set_linewidth(1.5)
    ax.set_facecolor("#f9fafb")
    ax.set_title("Distribution by Group", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_ylabel("Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.grid(axis="y", alpha=0.1, linestyle="--")

    # Bar chart with error bars
    ax = axes[1]
    bars = ax.bar(group_names, group_means, yerr=group_stds, capsize=6,
                  color=COLORS[:len(group_names)], alpha=0.85,
                  edgecolor="#667eea", linewidth=1.5,
                  error_kw=dict(elinewidth=1.5, ecolor="#667eea", capthick=0.5))
    ax.set_facecolor("#f9fafb")
    ax.set_title("Mean Comparison (± Std Dev)", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_ylabel("Mean Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.grid(axis="y", alpha=0.1, linestyle="--")
    for bar, m in zip(bars, group_means):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(group_stds) * 0.15,
                f"{m:.2f}", ha="center", va="bottom", fontsize=9, fontweight="600", color="#667eea")

    # KDE Density
    ax = axes[2]
    for idx, (name, data) in enumerate(group_data.items()):
        sns.kdeplot(data, ax=ax, label=name, color=COLORS[idx % len(COLORS)],
                    linewidth=2.5, fill=True, alpha=0.25)
    ax.set_facecolor("#f9fafb")
    ax.set_title("Density Distribution (KDE)", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_xlabel("Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.set_ylabel("Density", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.legend(fontsize=8.5, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", alpha=0.1, linestyle="--")

    plt.tight_layout(pad=2)
    st.pyplot(fig)

    # Descriptions
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="graph-description">
        <strong>📦 Distribution by Group:</strong> Box plot shows median (line), quartiles (box), and outliers for each group. 
        Helps identify skewness and variability patterns across groups.</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="graph-description">
        <strong>📈 Mean Comparison:</strong> Bar chart displays group means with standard deviation error bars. 
        Taller bars indicate higher average values.</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="graph-description">
        <strong>📊 Density Distribution:</strong> Smooth KDE curves show probability distribution. 
        Overlapping curves suggest groups may not differ significantly.</div>""", unsafe_allow_html=True)

    # ── Row 2: Histograms & Violin Plot ──
    st.markdown('<div style="margin-top:2.5rem"></div>', unsafe_allow_html=True)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.patch.set_facecolor("#ffffff")

    # Overlaid Histograms
    ax = axes[0]
    for idx, (name, data) in enumerate(group_data.items()):
        ax.hist(data, bins=8, alpha=0.6, label=name, color=COLORS[idx % len(COLORS)],
                edgecolor="#667eea", linewidth=0.5)
    ax.set_facecolor("#f9fafb")
    ax.set_title("Overlaid Histograms", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_xlabel("Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.set_ylabel("Frequency", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.legend(fontsize=8.5, framealpha=0.9)
    ax.grid(axis="y", alpha=0.1, linestyle="--")

    # Violin Plot
    ax = axes[1]
    parts = ax.violinplot([group_data[g] for g in group_names], positions=range(len(group_names)),
                          showmeans=True, showmedians=True, widths=0.7)
    for pc, color in zip(parts["bodies"], COLORS[:len(group_names)]):
        pc.set_facecolor(color)
        pc.set_alpha(0.75)
        pc.set_edgecolor("#667eea")
        pc.set_linewidth(1.2)
    parts["cmeans"].set_color("#667eea")
    parts["cmedians"].set_color("#1f2937")
    parts["cmeans"].set_linewidth(2)
    parts["cmedians"].set_linewidth(2)
    ax.set_xticks(range(len(group_names)))
    ax.set_xticklabels(group_names)
    ax.set_facecolor("#f9fafb")
    ax.set_title("Violin Plot (Distribution Shape)", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_ylabel("Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.grid(axis="y", alpha=0.1, linestyle="--")

    plt.tight_layout(pad=2)
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="graph-description">
        <strong>📚 Overlaid Histograms:</strong> Displays raw frequency counts with overlapping distributions. 
        Allows comparison of shapes and ranges between groups.</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="graph-description">
        <strong>🎻 Violin Plot:</strong> Combines box plot with KDE density curve. Shows full distribution shape 
        including bimodality and outliers for each group.</div>""", unsafe_allow_html=True)

    # ── Row 3: Swarm Plot & Summary Statistics ──
    st.markdown('<div style="margin-top:2.5rem"></div>', unsafe_allow_html=True)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.patch.set_facecolor("#ffffff")

    # Summary Statistics Heatmap
    ax = axes[0]
    summary_stats = []
    group_labels = []
    for idx, (name, data) in enumerate(group_data.items()):
        arr = np.array(data)
        summary_stats.append([arr.mean(), arr.std(ddof=1), len(arr)])
        group_labels.append(name)
    
    summary_array = np.array(summary_stats).T
    im = ax.imshow(summary_array, cmap='RdYlGn', aspect='auto', alpha=0.8)
    ax.set_xticks(range(len(group_labels)))
    ax.set_yticks(range(3))
    ax.set_xticklabels(group_labels, fontsize=9)
    ax.set_yticklabels(['Mean', 'Std Dev', 'Count'], fontsize=9)
    
    # Add values to heatmap
    for i in range(3):
        for j in range(len(group_labels)):
            text = ax.text(j, i, f'{summary_array[i, j]:.2f}',
                          ha="center", va="center", color="black", fontsize=9, fontweight="bold")
    
    ax.set_facecolor("#f9fafb")
    ax.set_title("Summary Statistics Heatmap", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    plt.colorbar(im, ax=ax, label="Value")

    # Range & Spread Plot
    ax = axes[1]
    for idx, (name, data) in enumerate(group_data.items()):
        arr = np.array(data)
        q1, median, q3 = np.percentile(arr, [25, 50, 75])
        iqr = q3 - q1
        
        # Plot range
        ax.plot([idx, idx], [arr.min(), arr.max()], 'o-', color=COLORS[idx % len(COLORS)],
               linewidth=2, markersize=6, alpha=0.6, label=name)
        # Plot IQR
        ax.fill_between([idx-0.1, idx+0.1], q1, q3, alpha=0.4, color=COLORS[idx % len(COLORS)])
        # Plot median
        ax.plot([idx-0.15, idx+0.15], [median, median], 'k-', linewidth=2.5)
    
    ax.set_xticks(range(len(group_labels)))
    ax.set_xticklabels(group_labels, fontsize=9)
    ax.set_facecolor("#f9fafb")
    ax.set_title("Range, IQR & Median", fontsize=12, fontweight="bold", color="#1f2937", pad=12)
    ax.set_ylabel("Value", fontsize=10, color="#1f2937", fontweight="500")
    ax.tick_params(colors="#6b7280", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#e5e7eb")
    ax.grid(axis="y", alpha=0.1, linestyle="--")

    plt.tight_layout(pad=2)
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="graph-description">
        <strong>🔥 Summary Statistics Heatmap:</strong> Displays mean, standard deviation, and sample size for each group. 
        Darker colors indicate higher values, making comparison easier.</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="graph-description">
        <strong>📊 Range & Spread:</strong> Shows full range (line ends), interquartile range (shaded box), and median (center line). 
        Reveals data spread without assuming normality.</div>""", unsafe_allow_html=True)

    # ── Statistical Tests & Assumptions ──
    st.markdown('<div style="margin-top:2.5rem"></div>', unsafe_allow_html=True)
    st.markdown("## 🔬 Statistical Tests & Assumptions")

    stat_col1, stat_col2 = st.columns(2)

    with stat_col1:
        st.markdown("### Homogeneity of Variance (Levene's Test)")
        # Levene's test
        levene_stat, levene_p = stats.levene(*group_data.values())
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Levene Test Statistic</div>
          <div class="value">{levene_stat:.4f}</div>
        </div>""", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">P-Value</div>
          <div class="value">{levene_p:.4f}</div>
        </div>""", unsafe_allow_html=True)
        if levene_p >= 0.05:
            st.markdown(f"""<div class="verdict-accept">
            ✅ <strong>Equal variances assumed</strong> (p = {levene_p:.4f} ≥ 0.05)
            Homogeneity assumption satisfied.</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="verdict-reject">
            ⚠️ <strong>Variances may differ</strong> (p = {levene_p:.4f} < 0.05)
            Consider Welch's ANOVA or transforming data.</div>""", unsafe_allow_html=True)

    with stat_col2:
        st.markdown("### Effect Size (Eta-Squared η²)")
        # Calculate eta-squared (effect size)
        grand_mean = np.mean(all_values)
        ss_between = sum(len(group_data[name]) * (np.mean(group_data[name]) - grand_mean)**2 
                        for name in group_data)
        ss_total = sum((val - grand_mean)**2 for val in all_values)
        eta_squared = ss_between / ss_total if ss_total > 0 else 0
        
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Eta-Squared (η²)</div>
          <div class="value">{eta_squared:.4f}</div>
        </div>""", unsafe_allow_html=True)
        
        if eta_squared < 0.01:
            effect_text = "🔍 **Negligible** effect size"
        elif eta_squared < 0.06:
            effect_text = "📊 **Small** effect size"
        elif eta_squared < 0.14:
            effect_text = "📈 **Medium** effect size"
        else:
            effect_text = "📊 **Large** effect size"
        
        st.markdown(f"""{effect_text}  
        Interpretation: {eta_squared*100:.2f}% of variance explained by group differences.""")

    # ── Descriptive Statistics Table ──
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)
    st.markdown("### Descriptive Statistics by Group")
    
    stats_data = []
    for name, data in group_data.items():
        arr = np.array(data)
        stats_data.append({
            "Group": name,
            "N": len(arr),
            "Mean": f"{arr.mean():.4f}",
            "Median": f"{np.median(arr):.4f}",
            "Std Dev": f"{arr.std(ddof=1):.4f}",
            "Min": f"{arr.min():.4f}",
            "Max": f"{arr.max():.4f}",
            "Q1": f"{np.percentile(arr, 25):.4f}",
            "Q3": f"{np.percentile(arr, 75):.4f}",
        })
    
    # Build table rows
    table_rows = ""
    for s in stats_data:
        table_rows += f"""<tr>
<td><strong>{s["Group"]}</strong></td>
<td>{s["N"]}</td>
<td>{s["Mean"]}</td>
<td>{s["Median"]}</td>
<td>{s["Std Dev"]}</td>
<td>{s["Min"]}</td>
<td>{s["Max"]}</td>
<td>{s["Q1"]}</td>
<td>{s["Q3"]}</td>
</tr>"""
    
    st.markdown(f"""<div class="table-wrapper"><table class="stats-table"><thead><tr><th>Group</th><th>N</th><th>Mean</th><th>Median</th><th>Std Dev</th><th>Min</th><th>Max</th><th>Q1</th><th>Q3</th></tr></thead><tbody>{table_rows}</tbody></table></div>""", unsafe_allow_html=True)

    # ── Insights ─────────────────────────────────────────────
    st.markdown('<div style="margin-top:2.5rem"></div>', unsafe_allow_html=True)
    st.markdown("## 💡 Key Insights & Recommendations")

    means_dict = {n: np.mean(d) for n, d in group_data.items()}
    best  = max(means_dict, key=means_dict.get)
    worst = min(means_dict, key=means_dict.get)

    if rejected:
        st.markdown(f"""
        <div class="insight-card">
          <strong>✘ SIGNIFICANT DIFFERENCE DETECTED</strong><br><br>
          🏆 <strong>{best}</strong> has the highest mean ({means_dict[best]:.4f}) and significantly 
          outperforms other groups.<br>
          📉 <strong>{worst}</strong> has the lowest mean ({means_dict[worst]:.4f}).<br><br>
          <strong>Statistical Evidence:</strong> F-statistic = {f_stat:.4f}, p-value = {p_value:.6f} < α = {a}<br>
          Effect Size (η²) = {eta_squared:.4f} ({("Large" if eta_squared >= 0.14 else ("Medium" if eta_squared >= 0.06 else ("Small" if eta_squared >= 0.01 else "Negligible")))}).<br><br>
          💡 <strong>Next Steps:</strong> Conduct post-hoc tests (Tukey HSD, Bonferroni) to identify which 
          specific pairs differ. Investigate factors contributing to {best}'s superior performance.
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="insight-card">
          <strong>✔ NO SIGNIFICANT DIFFERENCE DETECTED</strong><br><br>
          🤝 While <strong>{best}</strong> has the numerically highest mean ({means_dict[best]:.4f}) and 
          <strong>{worst}</strong> the lowest ({means_dict[worst]:.4f}), the difference is <strong>not statistically significant</strong>.<br><br>
          <strong>Statistical Evidence:</strong> F-statistic = {f_stat:.4f}, p-value = {p_value:.6f} ≥ α = {a}<br>
          Effect Size (η²) = {eta_squared:.4f} ({("Large" if eta_squared >= 0.14 else ("Medium" if eta_squared >= 0.06 else ("Small" if eta_squared >= 0.01 else "Negligible")))}).<br><br>
          💡 <strong>Interpretation:</strong> All groups perform comparably. Observed variation is likely due to 
          random chance. Increase sample size if you need to detect smaller differences.
        </div>""", unsafe_allow_html=True)

    # ── Summary Table ──
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)
    st.markdown("### ANOVA Summary (One-Way)")
    
    anova_summary_data = [
        {"Source": "Between Groups", "Sum of Squares": f"{sum(len(group_data[name]) * (np.mean(group_data[name]) - np.mean(all_values))**2 for name in group_data):.4f}", 
         "DF": len(group_data) - 1},
        {"Source": "Within Groups", "Sum of Squares": f"{sum(sum((val - np.mean(group_data[name]))**2 for val in group_data[name]) for name in group_data):.4f}", 
         "DF": len(all_values) - len(group_data)},
        {"Source": "Total", "Sum of Squares": f"{sum((val - np.mean(all_values))**2 for val in all_values):.4f}", 
         "DF": len(all_values) - 1},
    ]
    
    between_ms = float(anova_summary_data[0]["Sum of Squares"]) / max(anova_summary_data[0]["DF"], 1)
    within_ms = float(anova_summary_data[1]["Sum of Squares"]) / max(anova_summary_data[1]["DF"], 1)
    
    st.markdown(f"""<div class="table-wrapper"><table class="stats-table"><thead><tr><th>Source</th><th>Sum of Squares</th><th>Degrees of Freedom</th><th>Mean Square</th><th>F-Statistic</th><th>P-Value</th></tr></thead><tbody><tr><td><strong>Between Groups</strong></td><td>{anova_summary_data[0]["Sum of Squares"]}</td><td>{anova_summary_data[0]["DF"]}</td><td>{between_ms:.4f}</td><td rowspan="2" style="text-align: center; font-weight: bold; color: #667eea;"><strong>{f_stat:.4f}</strong></td><td rowspan="2" style="text-align: center; font-weight: bold; color: #667eea;"><strong>{p_value:.6f}</strong></td></tr><tr><td><strong>Within Groups</strong></td><td>{anova_summary_data[1]["Sum of Squares"]}</td><td>{anova_summary_data[1]["DF"]}</td><td>{within_ms:.4f}</td></tr><tr style="background: #f0f4ff !important;"><td><strong>Total</strong></td><td><strong>{anova_summary_data[2]["Sum of Squares"]}</strong></td><td><strong>{anova_summary_data[2]["DF"]}</strong></td><td>—</td><td colspan="2">—</td></tr></tbody></table></div>""", unsafe_allow_html=True)

    # ── Download Report ──
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)
    
    # Generate ALL visualizations for comprehensive PDF report
    fig_box_bytes = fig_bar_bytes = fig_kde_bytes = fig_hist_bytes = fig_violin_bytes = fig_heatmap_bytes = fig_range_bytes = None
    
    try:
        # 1. BoxPlot
        fig_box, ax = plt.subplots(figsize=(9, 4))
        bp = ax.boxplot([group_data[g] for g in group_names], labels=group_names, patch_artist=True,
                        widths=0.45, medianprops=dict(color="#667eea", linewidth=2.5),
                        whiskerprops=dict(linewidth=1.2, color="#9ca3af"), capprops=dict(linewidth=1.5, color="#9ca3af"),
                        flierprops=dict(marker="o", markersize=5, color="#d1d5db"))
        for patch, color in zip(bp["boxes"], COLORS):
            patch.set_facecolor(color); patch.set_alpha(0.75); patch.set_edgecolor("#667eea"); patch.set_linewidth(1.5)
        ax.set_facecolor("#f9fafb"); ax.set_title("Distribution by Group", fontsize=11, fontweight="bold", color="#1f2937")
        ax.set_ylabel("Value", fontsize=9, color="#1f2937"); ax.tick_params(colors="#6b7280", labelsize=8)
        ax.spines[["top", "right"]].set_visible(False); ax.spines[["left", "bottom"]].set_color("#e5e7eb")
        ax.grid(axis="y", alpha=0.1, linestyle="--"); plt.tight_layout()
        fig_box_bytes = io.BytesIO(); fig_box.savefig(fig_box_bytes, format='png', dpi=100, bbox_inches='tight'); fig_box_bytes.seek(0); plt.close(fig_box)
        
        # 2. Bar Chart
        fig_bar, ax = plt.subplots(figsize=(9, 4))
        bars = ax.bar(group_names, group_means, yerr=group_stds, capsize=6, color=COLORS[:len(group_names)], alpha=0.85,
                      edgecolor="#667eea", linewidth=1.5, error_kw=dict(elinewidth=1.5, ecolor="#667eea", capthick=0.5))
        ax.set_facecolor("#f9fafb"); ax.set_title("Mean Comparison (± Std Dev)", fontsize=11, fontweight="bold", color="#1f2937")
        ax.set_ylabel("Mean Value", fontsize=9, color="#1f2937"); ax.tick_params(colors="#6b7280", labelsize=8)
        ax.spines[["top", "right"]].set_visible(False); ax.spines[["left", "bottom"]].set_color("#e5e7eb")
        ax.grid(axis="y", alpha=0.1, linestyle="--")
        for bar, m in zip(bars, group_means):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(group_stds) * 0.15, f"{m:.2f}",
                   ha="center", va="bottom", fontsize=8, fontweight="600", color="#667eea")
        plt.tight_layout(); fig_bar_bytes = io.BytesIO(); fig_bar.savefig(fig_bar_bytes, format='png', dpi=100, bbox_inches='tight'); fig_bar_bytes.seek(0); plt.close(fig_bar)
        
        # 3. KDE Density
        fig_kde, ax = plt.subplots(figsize=(9, 4))
        for idx, (name, data) in enumerate(group_data.items()):
            sns.kdeplot(data, ax=ax, label=name, color=COLORS[idx % len(COLORS)], linewidth=2.2, fill=True, alpha=0.2)
        ax.set_facecolor("#f9fafb"); ax.set_title("Density Distribution (KDE)", fontsize=11, fontweight="bold", color="#1f2937")
        ax.set_xlabel("Value", fontsize=9, color="#1f2937"); ax.set_ylabel("Density", fontsize=9, color="#1f2937")
        ax.tick_params(colors="#6b7280", labelsize=8); ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#e5e7eb"); ax.legend(fontsize=8, framealpha=0.9, loc="upper right")
        ax.grid(axis="y", alpha=0.1, linestyle="--"); plt.tight_layout()
        fig_kde_bytes = io.BytesIO(); fig_kde.savefig(fig_kde_bytes, format='png', dpi=100, bbox_inches='tight'); fig_kde_bytes.seek(0); plt.close(fig_kde)
        
        # 4. Histogram
        fig_hist, ax = plt.subplots(figsize=(9, 4))
        for idx, (name, data) in enumerate(group_data.items()):
            ax.hist(data, bins=7, alpha=0.6, label=name, color=COLORS[idx % len(COLORS)], edgecolor="#667eea", linewidth=0.5)
        ax.set_facecolor("#f9fafb"); ax.set_title("Overlaid Histograms", fontsize=11, fontweight="bold", color="#1f2937")
        ax.set_xlabel("Value", fontsize=9, color="#1f2937"); ax.set_ylabel("Frequency", fontsize=9, color="#1f2937")
        ax.tick_params(colors="#6b7280", labelsize=8); ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#e5e7eb"); ax.legend(fontsize=8, framealpha=0.9)
        ax.grid(axis="y", alpha=0.1, linestyle="--"); plt.tight_layout()
        fig_hist_bytes = io.BytesIO(); fig_hist.savefig(fig_hist_bytes, format='png', dpi=100, bbox_inches='tight'); fig_hist_bytes.seek(0); plt.close(fig_hist)
        
        # 5. Violin Plot
        fig_violin, ax = plt.subplots(figsize=(9, 4))
        parts = ax.violinplot([group_data[g] for g in group_names], positions=range(len(group_names)))
        for pc in parts['bodies']:
            pc.set_facecolor('#6366f1'); pc.set_alpha(0.7); pc.set_edgecolor("#4f46e5"); pc.set_linewidth(1.5)
        ax.set_facecolor("#f9fafb"); ax.set_title("Violin Plot", fontsize=11, fontweight="bold", color="#1f2937")
        ax.set_xlabel("Group", fontsize=9, color="#1f2937"); ax.set_ylabel("Value", fontsize=9, color="#1f2937")
        ax.set_xticks(range(len(group_names))); ax.set_xticklabels(group_names, fontsize=8)
        ax.tick_params(colors="#6b7280", labelsize=8); ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#e5e7eb"); ax.grid(axis="y", alpha=0.1, linestyle="--")
        plt.tight_layout(); fig_violin_bytes = io.BytesIO(); fig_violin.savefig(fig_violin_bytes, format='png', dpi=100, bbox_inches='tight')
        fig_violin_bytes.seek(0); plt.close(fig_violin)
    except Exception as e:
        st.error(f"Error generating visualizations: {str(e)}")
        fig_box_bytes = fig_bar_bytes = fig_kde_bytes = fig_hist_bytes = fig_violin_bytes = None
    
    # ── Download Full PDF Report ──
    if PDF_AVAILABLE and fig_box_bytes:
        st.markdown('<div style="margin-top:2rem"></div>', unsafe_allow_html=True)
        st.markdown('<span class="section-label">📥 DOWNLOAD REPORT</span>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📄 Full Report (PDF)**", help="Download comprehensive ANOVA analysis report with all visualizations")
            try:
                pdf_buffer = io.BytesIO()
                doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, 
                                       leftMargin=0.75*inch, rightMargin=0.75*inch, 
                                       topMargin=0.75*inch, bottomMargin=0.75*inch)
                story = []
                styles = getSampleStyleSheet()
                
                # Title
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=24,
                    textColor=colors.HexColor("#6366f1"),
                    spaceAfter=12,
                    alignment=1,
                    fontName='Helvetica-Bold'
                )
                story.append(Paragraph("ANOVA Analysis Report", title_style))
                story.append(Spacer(1, 0.3*inch))
                
                # Metadata
                meta_style = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor("#6b7280"))
                story.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", meta_style))
                story.append(Paragraph(f"<b>Total Groups:</b> {len(group_names)} | <b>Observations:</b> {len(all_values)}", meta_style))
                story.append(Paragraph(f"<b>Significance Level:</b> {alpha}", meta_style))
                story.append(Spacer(1, 0.3*inch))
                
                # Statistical Summary Table
                story.append(Paragraph("Statistical Summary", styles['Heading2']))
                summary_data = [["Source", "Sum of Squares", "DF", "Mean Square", "F-Statistic", "P-Value"]]
                summary_data.append(["Between Groups", f"{anova_summary_data[0]['Sum of Squares']:.4f}", 
                                    f"{anova_summary_data[0]['DF']}", f"{between_ms:.4f}", f"{f_stat:.4f}", f"{p_value:.6f}"])
                summary_data.append(["Within Groups", f"{anova_summary_data[1]['Sum of Squares']:.4f}", 
                                    f"{anova_summary_data[1]['DF']}", f"{within_ms:.4f}", "—", "—"])
                summary_data.append(["Total", f"{anova_summary_data[2]['Sum of Squares']:.4f}", 
                                    f"{anova_summary_data[2]['DF']}", "—", "—", "—"])
                
                summary_table = Table(summary_data, colWidths=[1.2*inch, 1.3*inch, 0.6*inch, 1.1*inch, 1*inch, 1*inch])
                summary_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#6366f1")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#e5e7eb")),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
                ]))
                story.append(summary_table)
                story.append(Spacer(1, 0.3*inch))
                
                # Hypothesis Result
                result_text = f"<b>Result:</b> {'Reject H₀' if p_value < alpha else 'Fail to Reject H₀'} (p-value: {p_value:.6f} {'<' if p_value < alpha else '>'} α: {alpha})"
                result_style = ParagraphStyle('Result', parent=styles['Normal'], fontSize=11, 
                                             textColor=colors.HexColor("#ef4444" if p_value < alpha else "#10b981"),
                                             spaceAfter=12, fontName='Helvetica-Bold')
                story.append(Paragraph(result_text, result_style))
                story.append(Spacer(1, 0.3*inch))
                
                # Descriptive Statistics
                story.append(Paragraph("Group Descriptive Statistics", styles['Heading2']))
                desc_data = [["Group", "N", "Mean", "Std Dev", "Min", "Max"]]
                for name, data in group_data.items():
                    desc_data.append([name, str(len(data)), f"{np.mean(data):.4f}", f"{np.std(data):.4f}",
                                     f"{np.min(data):.4f}", f"{np.max(data):.4f}"])
                
                desc_table = Table(desc_data, colWidths=[1*inch, 0.7*inch, 1*inch, 1*inch, 1*inch, 1*inch])
                desc_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#6366f1")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#e5e7eb")),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
                ]))
                story.append(desc_table)
                story.append(PageBreak())
                
                # Add Visualizations
                if fig_box_bytes:
                    story.append(Paragraph("Distribution by Group (Box Plot)", styles['Heading2']))
                    story.append(Image(fig_box_bytes, width=6*inch, height=2.7*inch))
                    story.append(Spacer(1, 0.3*inch))
                
                if fig_bar_bytes:
                    story.append(Paragraph("Mean Comparison (Bar Chart)", styles['Heading2']))
                    story.append(Image(fig_bar_bytes, width=6*inch, height=2.7*inch))
                    story.append(Spacer(1, 0.3*inch))
                
                # Build PDF
                doc.build(story)
                pdf_buffer.seek(0)
                st.download_button(
                    label="📥 Download Full Report (PDF)",
                    data=pdf_buffer.getvalue(),
                    file_name=f"ANOVA_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf",
                    key="pdf_download"
                )
            except Exception as e:
                st.warning(f"⚠️ PDF Export not available: {str(e)}")
        
        with col2:
            st.markdown("**📋 Text Report (TXT)**", help="Download detailed text summary of ANOVA analysis")
            try:
                # Generate comprehensive text report
                txt_report = f"""
{'='*80}
                        ANOVA ANALYSIS REPORT
{'='*80}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{'─'*80}
ANALYSIS SUMMARY
{'─'*80}

Total Groups: {len(group_names)}
Total Observations: {len(all_values)}
Significance Level (α): {alpha}

{'─'*80}
GROUP INFORMATION
{'─'*80}

"""
                for name, data in group_data.items():
                    txt_report += f"""
Group: {name}
  Sample Size (n): {len(data)}
  Mean (μ): {np.mean(data):.6f}
  Standard Deviation (σ): {np.std(data):.6f}
  Variance (σ²): {np.var(data):.6f}
  Min Value: {np.min(data):.6f}
  Max Value: {np.max(data):.6f}
  Median: {np.median(data):.6f}
  Skewness: {stats.skew(data):.6f}
  Kurtosis: {stats.kurtosis(data):.6f}
"""
                
                txt_report += f"""
{'─'*80}
ANOVA RESULTS
{'─'*80}

F-Statistic: {f_stat:.6f}
P-Value: {p_value:.10f}
Alpha (Significance Level): {alpha}

Statistical Decision: {'REJECT H₀ (Significant difference exists between groups)' if p_value < alpha else 'FAIL TO REJECT H₀ (No significant difference between groups)'}

{'─'*80}
ANOVA TABLE
{'─'*80}

Source           | Sum of Squares | DF  | Mean Square | F-Statistic | P-Value
{'─'*80}
Between Groups   | {anova_summary_data[0]['Sum of Squares']:14.6f} | {anova_summary_data[0]['DF']:3.0f} | {between_ms:11.6f} | {f_stat:11.6f} | {p_value:.10f}
Within Groups    | {anova_summary_data[1]['Sum of Squares']:14.6f} | {anova_summary_data[1]['DF']:3.0f} | {within_ms:11.6f} |             |
Total            | {anova_summary_data[2]['Sum of Squares']:14.6f} | {anova_summary_data[2]['DF']:3.0f} |             |             |

{'─'*80}
INTERPRETATION
{'─'*80}

"""
                if p_value < alpha:
                    txt_report += f"""
✓ RESULT: REJECT THE NULL HYPOTHESIS
  
The p-value ({p_value:.6f}) is less than the significance level ({alpha}), 
indicating statistically significant differences exist between the group means.
There is strong evidence that at least one group mean differs from the others.
"""
                else:
                    txt_report += f"""
✗ RESULT: FAIL TO REJECT THE NULL HYPOTHESIS

The p-value ({p_value:.6f}) is greater than the significance level ({alpha}), 
indicating no statistically significant difference between group means.
The observed differences could reasonably be due to random variation.
"""
                
                txt_report += f"""

Effect Size (Eta-squared): {eta_squared:.6f}
Interpretation: {'Large effect' if eta_squared > 0.14 else 'Medium effect' if eta_squared > 0.06 else 'Small effect'}

{'═'*80}
End of Report
{'═'*80}
"""
                
                st.download_button(
                    label="📥 Download Text Report (TXT)",
                    data=txt_report,
                    file_name=f"ANOVA_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    key="txt_download"
                )
            except Exception as e:
                st.error(f"Error generating text report: {str(e)}")