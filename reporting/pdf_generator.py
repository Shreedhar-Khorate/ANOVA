"""
PDF Report Generator
"""

import io
from datetime import datetime
import numpy as np

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False


def generate_pdf_report(group_data, f_stat, p_value, alpha, eta_squared, levene_stat, levene_p,
                       all_values, anova_summary_data, between_ms, within_ms, 
                       fig_box_bytes=None, fig_bar_bytes=None):
    """
    Generate comprehensive PDF report.
    
    Args:
        group_data (dict): Dictionary with group data
        f_stat (float): F-statistic
        p_value (float): P-value
        alpha (float): Significance level
        eta_squared (float): Effect size
        levene_stat (float): Levene test statistic
        levene_p (float): Levene test p-value
        all_values (list): All combined values
        anova_summary_data (list): ANOVA summary table data
        between_ms (float): Between groups mean square
        within_ms (float): Within groups mean square
        fig_box_bytes (BytesIO): Box plot figure bytes
        fig_bar_bytes (BytesIO): Bar chart figure bytes
        
    Returns:
        bytes: PDF content as bytes, or None if not available
    """
    if not PDF_AVAILABLE:
        return None
    
    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer, pagesize=letter,
            leftMargin=0.75*inch, rightMargin=0.75*inch,
            topMargin=0.75*inch, bottomMargin=0.75*inch
        )
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle', parent=styles['Heading1'], fontSize=24,
            textColor=colors.HexColor('#6366f1'), spaceAfter=12,
            alignment=1, fontName='Helvetica-Bold'
        )
        heading_style = ParagraphStyle(
            'CustomHeading', parent=styles['Heading2'], fontSize=13,
            textColor=colors.HexColor('#6366f1'), spaceAfter=10, spaceBefore=10
        )
        normal_style = ParagraphStyle(
            'CustomNormal', parent=styles['Normal'], fontSize=9, spaceAfter=4
        )
        
        # Title
        story.append(Paragraph("📊 ANOVA Analysis Report", title_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Metadata
        meta_style = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=10,
                                   textColor=colors.HexColor("#6b7280"))
        story.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", meta_style))
        story.append(Paragraph(f"<b>Total Groups:</b> {len(group_data)} | <b>Observations:</b> {len(all_values)}", meta_style))
        story.append(Paragraph(f"<b>Significance Level:</b> {alpha}", meta_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Statistical Summary Table
        story.append(Paragraph("Statistical Summary", heading_style))
        summary_data = [["Source", "Sum of Squares", "DF", "Mean Square", "F-Statistic", "P-Value"]]
        summary_data.append(["Between Groups", f"{float(anova_summary_data[0]['Sum of Squares']):.4f}",
                           f"{anova_summary_data[0]['DF']}", f"{between_ms:.4f}",
                           f"{f_stat:.4f}", f"{p_value:.6f}"])
        summary_data.append(["Within Groups", f"{float(anova_summary_data[1]['Sum of Squares']):.4f}",
                           f"{anova_summary_data[1]['DF']}", f"{within_ms:.4f}", "—", "—"])
        summary_data.append(["Total", f"{float(anova_summary_data[2]['Sum of Squares']):.4f}",
                           f"{anova_summary_data[2]['DF']}", "—", "—", "—"])
        
        summary_table = Table(summary_data,
                            colWidths=[1.2*inch, 1.3*inch, 0.6*inch, 1.1*inch, 1*inch, 1*inch])
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
        story.append(Paragraph("Group Descriptive Statistics", heading_style))
        desc_data = [["Group", "N", "Mean", "Std Dev", "Min", "Max"]]
        for name, data in group_data.items():
            desc_data.append([name, str(len(data)), f"{np.mean(data):.4f}",
                            f"{np.std(data):.4f}", f"{np.min(data):.4f}", f"{np.max(data):.4f}"])
        
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
            story.append(Paragraph("Distribution by Group (Box Plot)", heading_style))
            story.append(Image(fig_box_bytes, width=6*inch, height=2.7*inch))
            story.append(Spacer(1, 0.3*inch))
        
        if fig_bar_bytes:
            story.append(Paragraph("Mean Comparison (Bar Chart)", heading_style))
            story.append(Image(fig_bar_bytes, width=6*inch, height=2.7*inch))
            story.append(Spacer(1, 0.3*inch))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    
    except Exception as e:
        print(f"PDF generation error: {str(e)}")
        return None
