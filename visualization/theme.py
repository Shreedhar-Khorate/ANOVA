"""
Theme & Color Schemes
"""

from config import GROUP_COLORS

# Export group colors
COLORS = GROUP_COLORS


def get_color_palette(num_colors=6):
    """
    Get a color palette with specified number of colors.
    
    Args:
        num_colors (int): Number of colors needed
        
    Returns:
        list: List of hex color codes
    """
    palette = COLORS * ((num_colors // len(COLORS)) + 1)
    return palette[:num_colors]


def get_color_by_index(index):
    """
    Get a color by index from the palette.
    
    Args:
        index (int): Index in the color palette
        
    Returns:
        str: Hex color code
    """
    return COLORS[index % len(COLORS)]
