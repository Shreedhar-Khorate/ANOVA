"""
Statistics Engine - Core ANOVA calculations and statistical functions
"""

import numpy as np
from scipy import stats


def run_anova(*groups):
    """
    Perform One-Way ANOVA test.
    
    Args:
        *groups: Variable number of group data lists
        
    Returns:
        tuple: (f_statistic, p_value)
    """
    return stats.f_oneway(*groups)


def calculate_effect_size(group_data: dict, all_values: list):
    """
    Calculate Eta-squared (η²) effect size.
    
    Args:
        group_data (dict): Dictionary with group names and data lists
        all_values (list): Combined list of all values
        
    Returns:
        float: Eta-squared value (0 to 1)
    """
    grand_mean = np.mean(all_values)
    ss_between = sum(
        len(group_data[name]) * (np.mean(group_data[name]) - grand_mean) ** 2
        for name in group_data
    )
    ss_total = sum((val - grand_mean) ** 2 for val in all_values)
    
    if ss_total == 0:
        return 0
    
    eta_squared = ss_between / ss_total
    return float(eta_squared)


def calculate_levene_test(*groups):
    """
    Perform Levene's test for homogeneity of variance.
    
    Args:
        *groups: Variable number of group data lists
        
    Returns:
        tuple: (test_statistic, p_value)
    """
    return stats.levene(*groups)


def calculate_descriptive_stats(group_data: dict):
    """
    Calculate comprehensive descriptive statistics for all groups.
    
    Args:
        group_data (dict): Dictionary with group names and data lists
        
    Returns:
        dict: Descriptive statistics for each group
    """
    stats_dict = {}
    
    for name, data in group_data.items():
        arr = np.array(data)
        stats_dict[name] = {
            "n": len(arr),
            "mean": float(arr.mean()),
            "median": float(np.median(arr)),
            "std": float(arr.std(ddof=1)),
            "variance": float(arr.var(ddof=1)),
            "min": float(arr.min()),
            "max": float(arr.max()),
            "q1": float(np.percentile(arr, 25)),
            "q3": float(np.percentile(arr, 75)),
            "iqr": float(np.percentile(arr, 75) - np.percentile(arr, 25)),
            "skewness": float(stats.skew(arr)),
            "kurtosis": float(stats.kurtosis(arr)),
        }
    
    return stats_dict


def calculate_anova_table(group_data: dict, all_values: list):
    """
    Calculate complete ANOVA table.
    
    Args:
        group_data (dict): Dictionary with group names and data lists
        all_values (list): Combined list of all values
        
    Returns:
        dict: ANOVA table with all components
    """
    grand_mean = np.mean(all_values)
    
    # Sum of Squares
    ss_between = sum(
        len(group_data[name]) * (np.mean(group_data[name]) - grand_mean) ** 2
        for name in group_data
    )
    ss_within = sum(
        sum((val - np.mean(group_data[name])) ** 2 for val in group_data[name])
        for name in group_data
    )
    ss_total = sum((val - grand_mean) ** 2 for val in all_values)
    
    # Degrees of Freedom
    k = len(group_data)  # number of groups
    n = len(all_values)   # total observations
    df_between = k - 1
    df_within = n - k
    df_total = n - 1
    
    # Mean Squares
    ms_between = ss_between / max(df_between, 1)
    ms_within = ss_within / max(df_within, 1)
    
    # F-statistic and p-value
    f_stat, p_value = run_anova(*group_data.values())
    
    return {
        "ss_between": float(ss_between),
        "ss_within": float(ss_within),
        "ss_total": float(ss_total),
        "df_between": df_between,
        "df_within": df_within,
        "df_total": df_total,
        "ms_between": float(ms_between),
        "ms_within": float(ms_within),
        "f_statistic": float(f_stat),
        "p_value": float(p_value),
    }


def interpret_effect_size(eta_squared: float):
    """
    Interpret effect size magnitude.
    
    Args:
        eta_squared (float): Eta-squared value
        
    Returns:
        str: Interpretation (Negligible, Small, Medium, or Large)
    """
    from config import EFFECT_SIZE_NEGLIGIBLE, EFFECT_SIZE_SMALL, EFFECT_SIZE_MEDIUM
    
    if eta_squared < EFFECT_SIZE_NEGLIGIBLE:
        return "Negligible"
    elif eta_squared < EFFECT_SIZE_SMALL:
        return "Small"
    elif eta_squared < EFFECT_SIZE_MEDIUM:
        return "Medium"
    else:
        return "Large"


def get_group_comparison(group_data: dict):
    """
    Compare group means to identify best and worst performers.
    
    Args:
        group_data (dict): Dictionary with group names and data lists
        
    Returns:
        dict: Comparison results with best, worst, and mean values
    """
    means = {name: np.mean(data) for name, data in group_data.items()}
    best = max(means, key=means.get)
    worst = min(means, key=means.get)
    
    return {
        "all_means": means,
        "best_group": best,
        "best_value": means[best],
        "worst_group": worst,
        "worst_value": means[worst],
        "difference": means[best] - means[worst],
    }
