"""
pages/03_results.py - Results, Visualizations & Reports Section
"""

import streamlit as st
import numpy as np
from datetime import datetime
import io

from visualization import COLORS
from utils.stats_engine import (
    calculate_effect_size, calculate_levene_test,
    calculate_anova_table, interpret_effect_size
)
from visualization.charts import (
    create_boxplot, create_barchart, create_kde_plot,
    create_histogram, create_violin_plot
)


def show_results():
    """Display results, visualizations, and reports."""
    
    if "anova_results" not in st.session_state:
        st.info("👈 Complete the analysis on the left to see results here.")
        return
    
    res = st.session_state["anova_results"]
    group_data = res["group_data"]
    f_stat = res["f_stat"]
    p_value = res["p_value"]
    a = res["alpha"]
    group_names = res["group_names"]
    group_means = res["group_means"]
    group_stds = res["group_stds"]
    rejected = p_value < a
    
    all_values = np.array([v for data in group_data.values() for v in data])

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Analysis Results</p>', unsafe_allow_html=True)

    # ── Key Metrics (Responsive) ──
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.metric("F-Statistic", f"{f_stat:.4f}")
    with m2:
        st.metric("P-Value", f"{p_value:.4f}")
    with m3:
        st.metric("Alpha (α)", f"{a}")
    with m4:
        st.metric("Groups", len(group_data))
    with m5:
        sig_text = "✔ YES" if rejected else "✘ NO"
        st.metric("Significant", sig_text)

    st.markdown('<div style="margin-top:1.25rem"></div>', unsafe_allow_html=True)

    # ── Statistical Decision ──
    if rejected:
        st.success(f"✘ **Reject H₀** — Statistically significant difference exists (p = {p_value:.6f} < α = {a})")
    else:
        st.info(f"✔ **Fail to Reject H₀** — No significant difference (p = {p_value:.6f} ≥ α = {a})")

    # ── Group Summary ─
    st.markdown("### Group Summary")
    tile_cols = st.columns(len(group_data))
    for idx, (name, data) in enumerate(group_data.items()):
        arr = np.array(data)
        with tile_cols[idx]:
            st.metric(
                name,
                f"μ = {arr.mean():.4f}",
                f"n = {len(arr)}, σ = {arr.std(ddof=1):.4f}"
            )

    # ── Visualizations (Using Modular Functions) ──
    st.markdown("## 📊 Visualizations")
    
    try:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Box Plot")
            fig_box_bytes = create_boxplot(group_data, group_names, COLORS)
            st.image(fig_box_bytes)
        
        with col2:
            st.subheader("Bar Chart")
            fig_bar_bytes = create_barchart(group_names, group_means, group_stds, COLORS)
            st.image(fig_bar_bytes)
        
        with col3:
            st.subheader("KDE Plot")
            fig_kde_bytes = create_kde_plot(group_data, COLORS)
            st.image(fig_kde_bytes)
        
        col4, col5 = st.columns(2)
        with col4:
            st.subheader("Histogram")
            fig_hist_bytes = create_histogram(group_data, COLORS)
            st.image(fig_hist_bytes)
        
        with col5:
            st.subheader("Violin Plot")
            fig_violin_bytes = create_violin_plot(group_data, group_names, COLORS)
            st.image(fig_violin_bytes)
            
    except Exception as e:
        st.error(f"⚠️ Visualization error: {str(e)}")

    # ── Statistical Tests & Assumptions ──
    st.markdown("## 🔬 Statistical Tests")
    
    stat_col1, stat_col2 = st.columns(2)
    
    with stat_col1:
        st.subheader("Levene's Test")
        levene_stat, levene_p = calculate_levene_test(*group_data.values())
        st.metric("Test Statistic", f"{levene_stat:.4f}")
        st.metric("P-Value", f"{levene_p:.4f}")
        if levene_p >= 0.05:
            st.success(f"✅ Equal variances assumed (p ≥ 0.05)")
        else:
            st.warning(f"⚠️ Variances may differ (p < 0.05)")
    
    with stat_col2:
        st.subheader("Effect Size (Eta-Squared)")
        eta_squared = calculate_effect_size(group_data, all_values)
        st.metric("η²", f"{eta_squared:.4f}")
        st.info(f"**{interpret_effect_size(eta_squared)}** — {eta_squared*100:.2f}% variance explained")

    # ── Descriptive Statistics ──
    st.markdown("### Descriptive Statistics")
    
    stats_df_data = []
    for name, data in group_data.items():
        arr = np.array(data)
        stats_df_data.append({
            "Group": name,
            "N": len(arr),
            "Mean": f"{arr.mean():.4f}",
            "Median": f"{np.median(arr):.4f}",
            "Std Dev": f"{arr.std(ddof=1):.4f}",
            "Min": f"{arr.min():.4f}",
            "Max": f"{arr.max():.4f}",
        })
    
    st.dataframe(stats_df_data, use_container_width=True)

    # ── Insights ──
    st.markdown("## 💡 Insights")
    
    means_dict = {n: np.mean(d) for n, d in group_data.items()}
    best = max(means_dict, key=means_dict.get)
    worst = min(means_dict, key=means_dict.get)
    
    if rejected:
        st.success(f"""
        **✘ SIGNIFICANT DIFFERENCE DETECTED**
        
        🏆 **{best}** has the highest mean ({means_dict[best]:.4f})  
        📉 **{worst}** has the lowest mean ({means_dict[worst]:.4f})
        
        **F-statistic:** {f_stat:.4f} | **p-value:** {p_value:.6f}  
        **Effect Size:** {interpret_effect_size(eta_squared)}
        """)
    else:
        st.info(f"""
        **✔ NO SIGNIFICANT DIFFERENCE DETECTED**
        
        🤝 While **{best}** has the highest mean ({means_dict[best]:.4f}),  
        the difference is **not statistically significant**.
        
        **F-statistic:** {f_stat:.4f} | **p-value:** {p_value:.6f}  
        **Effect Size:** {interpret_effect_size(eta_squared)}
        """)

    # ── ANOVA Summary Table ──
    st.markdown("### ANOVA Table")
    
    anova_table = calculate_anova_table(group_data, all_values)
    
    anova_df = {
        "Source": ["Between Groups", "Within Groups", "Total"],
        "Sum of Squares": [
            f"{anova_table['ss_between']:.4f}",
            f"{anova_table['ss_within']:.4f}",
            f"{anova_table['ss_total']:.4f}"
        ],
        "DF": [
            anova_table['df_between'],
            anova_table['df_within'],
            anova_table['df_total']
        ],
        "Mean Square": [
            f"{anova_table['ms_between']:.4f}",
            f"{anova_table['ms_within']:.4f}",
            "—"
        ],
        "F-Statistic": [f"{f_stat:.4f}", "—", "—"],
        "P-Value": [f"{p_value:.6f}", "—", "—"]
    }
    
    st.dataframe(anova_df, use_container_width=True)

    # ── Download Report ──
    st.markdown("## 📥 Download Report")
    
    # Check for ReportLab
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib import colors
        PDF_AVAILABLE = True
    except ImportError:
        PDF_AVAILABLE = False
    
    col1, col2 = st.columns(2)
    
    with col1:
        if PDF_AVAILABLE:
            try:
                pdf_buffer = io.BytesIO()
                doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
                story = []
                styles = getSampleStyleSheet()
                
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=24,
                    textColor=colors.HexColor("#6366f1"),
                    spaceAfter=12,
                    alignment=1,
                )
                story.append(Paragraph("ANOVA Analysis Report", title_style))
                story.append(Spacer(1, 0.2*inch))
                
                story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
                story.append(Paragraph(f"Groups: {len(group_names)} | Observations: {len(all_values)}", styles['Normal']))
                story.append(Spacer(1, 0.3*inch))
                
                # ANOVA table
                story.append(Paragraph("ANOVA Summary", styles['Heading2']))
                table_data = [
                    ["Source", "SS", "DF", "MS", "F", "P-Value"],
                    ["Between Groups", f"{anova_table['ss_between']:.4f}", str(anova_table['df_between']), 
                     f"{anova_table['ms_between']:.4f}", f"{f_stat:.4f}", f"{p_value:.6f}"],
                    ["Within Groups", f"{anova_table['ss_within']:.4f}", str(anova_table['df_within']),
                     f"{anova_table['ms_within']:.4f}", "—", "—"],
                    ["Total", f"{anova_table['ss_total']:.4f}", str(anova_table['df_total']), "—", "—", "—"],
                ]
                table = Table(table_data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#6366f1")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                story.append(table)
                
                doc.build(story)
                pdf_buffer.seek(0)
                st.download_button(
                    label="📥 Download PDF Report",
                    data=pdf_buffer.getvalue(),
                    file_name=f"ANOVA_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.warning(f"PDF export unavailable: {str(e)}")
        else:
            st.warning("ReportLab not installed. Install with: pip install reportlab")
    
    with col2:
        try:
            txt_report = f"""ANOVA ANALYSIS REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ANALYSIS SUMMARY
Groups: {len(group_names)}
Total Observations: {len(all_values)}
Significance Level: {a}

ANOVA RESULTS
F-Statistic: {f_stat:.6f}
P-Value: {p_value:.10f}
Result: {'REJECT H₀' if p_value < a else 'FAIL TO REJECT H₀'}

ANOVA TABLE
Source|SS|DF|MS|F|P-Value
Between Groups|{anova_table['ss_between']:.4f}|{anova_table['df_between']}|{anova_table['ms_between']:.4f}|{f_stat:.4f}|{p_value:.6f}
Within Groups|{anova_table['ss_within']:.4f}|{anova_table['df_within']}|{anova_table['ms_within']:.4f}|—|—
Total|{anova_table['ss_total']:.4f}|{anova_table['df_total']}|—|—|—
"""
            
            st.download_button(
                label="📥 Download Text Report",
                data=txt_report,
                file_name=f"ANOVA_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error generating text report: {str(e)}")
