"""
Text Report Generator
"""

from datetime import datetime
import numpy as np
from scipy import stats


def generate_txt_report(group_data, f_stat, p_value, alpha, eta_squared, levene_stat, levene_p,
                       all_values, anova_summary_data, between_ms, within_ms):
    """
    Generate comprehensive text report.
    
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
        
    Returns:
        str: Text report content
    """
    report = f"""
{'='*80}
                        ANOVA ANALYSIS REPORT
{'='*80}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{'─'*80}
ANALYSIS SUMMARY
{'─'*80}

Total Groups: {len(group_data)}
Total Observations: {len(all_values)}
Significance Level (α): {alpha}

{'─'*80}
GROUP INFORMATION
{'─'*80}

"""
    
    for name, data in group_data.items():
        report += f"""
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
    
    report += f"""
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
Between Groups   | {float(anova_summary_data[0]['Sum of Squares']):14.6f} | {anova_summary_data[0]['DF']:3.0f} | {between_ms:11.6f} | {f_stat:11.6f} | {p_value:.10f}
Within Groups    | {float(anova_summary_data[1]['Sum of Squares']):14.6f} | {anova_summary_data[1]['DF']:3.0f} | {within_ms:11.6f} |             |
Total            | {float(anova_summary_data[2]['Sum of Squares']):14.6f} | {anova_summary_data[2]['DF']:3.0f} |             |             |

{'─'*80}
ASSUMPTION TESTING
{'─'*80}

Levene's Test for Homogeneity of Variance:
  Test Statistic: {levene_stat:.6f}
  P-Value: {levene_p:.6f}
  Result: {'✅ Equal variances (p ≥ 0.05)' if levene_p >= 0.05 else '⚠️ Unequal variances (p < 0.05)'}

{'─'*80}
EFFECT SIZE
{'─'*80}

Eta-squared (η²): {eta_squared:.6f}
Interpretation: {'Large effect' if eta_squared > 0.14 else 'Medium effect' if eta_squared > 0.06 else 'Small effect'}
Variance Explained: {eta_squared*100:.2f}%

{'─'*80}
INTERPRETATION
{'─'*80}

"""
    
    if p_value < alpha:
        report += f"""
✓ RESULT: REJECT THE NULL HYPOTHESIS
  
The p-value ({p_value:.6f}) is less than the significance level ({alpha}), 
indicating statistically significant differences exist between the group means.
There is strong evidence that at least one group mean differs from the others.
"""
    else:
        report += f"""
✗ RESULT: FAIL TO REJECT THE NULL HYPOTHESIS

The p-value ({p_value:.6f}) is greater than the significance level ({alpha}), 
indicating no statistically significant difference between group means.
The observed differences could reasonably be due to random variation.
"""
    
    report += f"""

{'═'*80}
End of Report
{'═'*80}
"""
    
    return report
