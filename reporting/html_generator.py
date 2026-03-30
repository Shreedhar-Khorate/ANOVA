"""
HTML Report Generator
"""

from datetime import datetime
import numpy as np


def generate_html_report(group_data, f_stat, p_value, alpha, all_values, eta_squared, 
                        levene_stat, levene_p):
    """
    Generate comprehensive HTML report.
    
    Args:
        group_data (dict): Dictionary with group data
        f_stat (float): F-statistic
        p_value (float): P-value
        alpha (float): Significance level
        all_values (list): All combined values
        eta_squared (float): Effect size
        levene_stat (float): Levene test statistic
        levene_p (float): Levene test p-value
        
    Returns:
        str: HTML report content
    """
    rejected = p_value < alpha
    means_dict = {n: np.mean(d) for n, d in group_data.items()}
    best = max(means_dict, key=means_dict.get)
    worst = min(means_dict, key=means_dict.get)
    variance_result = '✅ Equal variances assumed (p ≥ 0.05)' if levene_p >= 0.05 else '⚠️ Variances may differ (p < 0.05)'
    
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
        .insight {{
            background: #fffbeb;
            border-left: 4px solid #fcd34d;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            color: #78350f;
        }}
        .footer {{
            text-align: center;
            color: #6b7280;
            border-top: 1px solid #e5e7eb;
            padding-top: 20px;
            margin-top: 40px;
            font-size: 0.9rem;
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
        <div class="insight">
            <strong>{'Significant Difference Detected' if rejected else 'No Significant Difference'}</strong><br><br>
            🏆 <strong>{best}</strong> has the highest mean ({means_dict[best]:.4f})<br>
            📉 <strong>{worst}</strong> has the lowest mean ({means_dict[worst]:.4f})<br><br>
            Effect Size: {'Large' if eta_squared >= 0.14 else ('Medium' if eta_squared >= 0.06 else ('Small' if eta_squared >= 0.01 else 'Negligible'))} ({eta_squared*100:.2f}% variance explained)<br><br>
            <strong>Recommendation:</strong> {'Conduct post-hoc tests (Tukey HSD, Bonferroni) to identify specific group differences.' if rejected else 'Increase sample size if attempting to detect smaller differences.'}
        </div>
    </div>

    <div class="footer">
        <p>ANOVA Analysis Tool | Statistical Analysis Report</p>
    </div>
</body>
</html>
"""
    
    return html
