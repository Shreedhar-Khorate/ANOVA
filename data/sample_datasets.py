"""
Sample Datasets for ANOVA Analysis
"""

from config import (
    SAMPLE_DATASET_EXAM,
    SAMPLE_DATASET_YIELD,
    SAMPLE_DATASET_SIMILAR,
)

SAMPLE_DATASETS = {
    SAMPLE_DATASET_EXAM: {
        "Method A": [85, 90, 78, 92, 88, 76, 95, 89],
        "Method B": [70, 65, 72, 68, 74, 71, 69, 73],
        "Method C": [80, 82, 79, 85, 83, 81, 78, 84],
    },
    SAMPLE_DATASET_YIELD: {
        "Fertilizer X": [20, 22, 19, 24, 25, 21, 23],
        "Fertilizer Y": [28, 30, 27, 26, 29, 31, 32],
        "Fertilizer Z": [22, 23, 21, 20, 24, 22, 25],
    },
    SAMPLE_DATASET_SIMILAR: {
        "Group 1": [50, 52, 48, 51, 49, 53, 50],
        "Group 2": [51, 49, 50, 52, 48, 50, 51],
        "Group 3": [50, 51, 49, 52, 50, 48, 51],
    },
}


def get_sample_datasets():
    """
    Get all available sample datasets.
    
    Returns:
        dict: Dictionary of sample datasets
    """
    return SAMPLE_DATASETS


def get_dataset_names():
    """
    Get names of all available sample datasets.
    
    Returns:
        list: List of dataset names
    """
    return list(SAMPLE_DATASETS.keys())


def load_sample_dataset(name):
    """
    Load a specific sample dataset by name.
    
    Args:
        name (str): Name of the dataset
        
    Returns:
        dict: Dataset if found, None otherwise
    """
    return SAMPLE_DATASETS.get(name)
