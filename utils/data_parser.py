"""
Data Parser - Input parsing and processing functions
"""

from config import MIN_VALUES_PER_GROUP


def parse_input(text: str):
    """
    Parse comma-separated text input into a list of floats.
    
    Args:
        text (str): Comma-separated numeric values
        
    Returns:
        list: List of floats if valid, None otherwise
    """
    text = text.strip()
    if not text:
        return None
    try:
        values = [float(x.strip()) for x in text.split(",") if x.strip()]
        return values if len(values) >= MIN_VALUES_PER_GROUP else None
    except ValueError:
        return None


def format_number(value, decimals=4):
    """
    Format a number to specified decimal places.
    
    Args:
        value (float): Number to format
        decimals (int): Number of decimal places
        
    Returns:
        str: Formatted number
    """
    return f"{value:.{decimals}f}"


def get_summary_stats(data):
    """
    Get basic summary statistics for a dataset.
    
    Args:
        data (list): List of numeric values
        
    Returns:
        dict: Dictionary with count, mean, std, min, max
    """
    import numpy as np
    
    arr = np.array(data)
    return {
        "count": len(arr),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=1)),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }
