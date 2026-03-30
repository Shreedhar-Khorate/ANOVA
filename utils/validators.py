"""
Data Validators - Validation functions for input data
"""

import numpy as np
from config import MIN_VALUES_PER_GROUP, MIN_DATA_POINTS_TOTAL


def validate_input(text: str):
    """
    Validate raw text input.
    
    Args:
        text (str): Raw text input
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "Input cannot be empty"
    
    try:
        values = [float(x.strip()) for x in text.split(",") if x.strip()]
    except ValueError:
        return False, "Invalid numeric values"
    
    if len(values) < MIN_VALUES_PER_GROUP:
        return False, f"Need at least {MIN_VALUES_PER_GROUP} values"
    
    return True, None


def validate_group_data(group_data: dict):
    """
    Validate complete group data dictionary.
    
    Args:
        group_data (dict): Dictionary with group names as keys and data lists as values
        
    Returns:
        tuple: (is_valid, error_message, total_points)
    """
    if len(group_data) < 2:
        return False, "Need at least 2 groups", 0
    
    total_points = sum(len(data) for data in group_data.values())
    
    if total_points < MIN_DATA_POINTS_TOTAL:
        return False, f"Need at least {MIN_DATA_POINTS_TOTAL} total data points", total_points
    
    return True, None, total_points


def check_normality_assumption(data, alpha=0.05):
    """
    Simple normality check using Shapiro-Wilk test.
    
    Args:
        data (list or array): Data to test
        alpha (float): Significance level
        
    Returns:
        dict: Test results with statistic, p-value, and interpretation
    """
    from scipy import stats
    
    arr = np.array(data)
    if len(arr) < 3:
        return {"statistic": None, "p_value": None, "is_normal": True, "note": "Too few samples"}
    
    stat, p_value = stats.shapiro(arr)
    is_normal = p_value >= alpha
    
    return {
        "statistic": stat,
        "p_value": p_value,
        "is_normal": is_normal,
        "interpretation": "✅ Normal" if is_normal else "⚠️ Non-normal",
    }


def check_group_sizes(group_data: dict):
    """
    Check if group sizes are reasonably balanced.
    
    Args:
        group_data (dict): Dictionary with group names and data
        
    Returns:
        dict: Analysis of group size balance
    """
    sizes = {name: len(data) for name, data in group_data.items()}
    max_size = max(sizes.values())
    min_size = min(sizes.values())
    ratio = max_size / min_size if min_size > 0 else float('inf')
    
    is_balanced = ratio <= 2.0  # Groups within 2x ratio are considered balanced
    
    return {
        "sizes": sizes,
        "max_size": max_size,
        "min_size": min_size,
        "ratio": ratio,
        "is_balanced": is_balanced,
        "interpretation": "✅ Balanced" if is_balanced else "⚠️ Imbalanced",
    }
