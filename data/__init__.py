"""
Data module for ANOVA Analysis Tool
"""

from .sample_datasets import SAMPLE_DATASETS, get_dataset_names, load_sample_dataset

__all__ = [
    "SAMPLE_DATASETS",
    "get_dataset_names",
    "load_sample_dataset",
]
