"""
Chart Generation - Matplotlib visualization functions
"""

import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from config import (
    PLOT_DPI,
    PLOT_FORMAT,
    PLOT_BBOX,
    FONTSIZE_TITLE,
    FONTSIZE_HEADING,
    FONTSIZE_LABEL,
    FONTSIZE_TICK,
    FONTSIZE_LEGEND,
    PRIMARY_COLOR,
    PRIMARY_DARK,
    LIGHT_COLOR,
    DARK_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    GRID_ALPHA,
    GRID_LINESTYLE,
)
from .theme import get_color_palette


def _setup_plot_style():
    """Setup common plot styling."""
    sns.set_theme(style="white", palette="muted")
    return get_color_palette(6)


def _apply_common_styling(ax, title):
    """Apply common styling to a plot axis."""
    ax.set_facecolor(LIGHT_COLOR)
    ax.set_title(title, fontsize=FONTSIZE_HEADING, fontweight="bold", color=DARK_COLOR, pad=12)
    ax.tick_params(colors=TEXT_COLOR, labelsize=FONTSIZE_TICK)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(BORDER_COLOR)
    ax.grid(axis="y", alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)


def _get_fig_bytes(fig):
    """Convert matplotlib figure to BytesIO object."""
    fig_bytes = io.BytesIO()
    fig.savefig(fig_bytes, format=PLOT_FORMAT, dpi=PLOT_DPI, bbox_inches=PLOT_BBOX)
    fig_bytes.seek(0)
    plt.close(fig)
    return fig_bytes


def create_boxplot(group_data, group_names, colors):
    """
    Create a box plot for distribution comparison.
    
    Args:
        group_data (dict): Groups with data lists
        group_names (list): List of group names
        colors (list): List of colors for groups
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    bp = ax.boxplot(
        [group_data[g] for g in group_names],
        labels=group_names,
        patch_artist=True,
        widths=0.45,
        medianprops=dict(color=PRIMARY_COLOR, linewidth=2.5),
        whiskerprops=dict(linewidth=1.2, color="gray"),
        capprops=dict(linewidth=1.5, color="gray"),
        flierprops=dict(marker="o", markersize=5, color="lightgray"),
    )
    
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
        patch.set_edgecolor(PRIMARY_COLOR)
        patch.set_linewidth(1.5)
    
    _apply_common_styling(ax, "Distribution by Group")
    ax.set_ylabel("Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_barchart(group_names, means, stds, colors):
    """
    Create a bar chart with error bars.
    
    Args:
        group_names (list): Group names
        means (list): Mean values
        stds (list): Standard deviations
        colors (list): Colors for bars
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    bars = ax.bar(
        group_names, means, yerr=stds, capsize=6,
        color=colors[:len(group_names)], alpha=0.85,
        edgecolor=PRIMARY_COLOR, linewidth=1.5,
        error_kw=dict(elinewidth=1.5, ecolor=PRIMARY_COLOR, capthick=0.5)
    )
    
    for bar, m in zip(bars, means):
        ax.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + max(stds) * 0.15,
            f"{m:.2f}", ha="center", va="bottom", fontsize=9, fontweight="600", color=PRIMARY_COLOR
        )
    
    _apply_common_styling(ax, "Mean Comparison (± Std Dev)")
    ax.set_ylabel("Mean Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_kde_plot(group_data, colors):
    """
    Create a kernel density estimation plot.
    
    Args:
        group_data (dict): Groups with data lists
        colors (list): Colors for groups
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    for idx, (name, data) in enumerate(group_data.items()):
        sns.kdeplot(
            data, ax=ax, label=name, color=colors[idx % len(colors)],
            linewidth=2.2, fill=True, alpha=0.2
        )
    
    _apply_common_styling(ax, "Density Distribution (KDE)")
    ax.set_xlabel("Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    ax.set_ylabel("Density", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    ax.legend(fontsize=FONTSIZE_LEGEND, framealpha=0.9, loc="upper right")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_histogram(group_data, colors):
    """
    Create overlaid histograms for groups.
    
    Args:
        group_data (dict): Groups with data lists
        colors (list): Colors for groups
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    for idx, (name, data) in enumerate(group_data.items()):
        ax.hist(
            data, bins=7, alpha=0.6, label=name,
            color=colors[idx % len(colors)], edgecolor=PRIMARY_COLOR, linewidth=0.5
        )
    
    _apply_common_styling(ax, "Overlaid Histograms")
    ax.set_xlabel("Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    ax.set_ylabel("Frequency", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    ax.legend(fontsize=FONTSIZE_LEGEND, framealpha=0.9)
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_violin_plot(group_data, group_names, colors):
    """
    Create a violin plot for distribution shape analysis.
    
    Args:
        group_data (dict): Groups with data lists
        group_names (list): List of group names
        colors (list): Colors for groups
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    parts = ax.violinplot(
        [group_data[g] for g in group_names],
        positions=range(len(group_names)),
        showmeans=True, showmedians=True, widths=0.7
    )
    
    for pc, color in zip(parts["bodies"], colors[:len(group_names)]):
        pc.set_facecolor(color)
        pc.set_alpha(0.75)
        pc.set_edgecolor(PRIMARY_COLOR)
        pc.set_linewidth(1.2)
    
    parts["cmeans"].set_color(PRIMARY_COLOR)
    parts["cmedians"].set_color(DARK_COLOR)
    parts["cmeans"].set_linewidth(2)
    parts["cmedians"].set_linewidth(2)
    
    ax.set_xticks(range(len(group_names)))
    ax.set_xticklabels(group_names)
    
    _apply_common_styling(ax, "Violin Plot (Distribution Shape)")
    ax.set_ylabel("Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_heatmap(group_data):
    """
    Create a heatmap of summary statistics.
    
    Args:
        group_data (dict): Groups with data lists
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#ffffff")
    
    summary_stats = []
    group_labels = []
    for name, data in group_data.items():
        arr = np.array(data)
        summary_stats.append([arr.mean(), arr.std(ddof=1), len(arr)])
        group_labels.append(name)
    
    summary_array = np.array(summary_stats).T
    im = ax.imshow(summary_array, cmap="RdYlGn", aspect="auto", alpha=0.8)
    
    ax.set_xticks(range(len(group_labels)))
    ax.set_yticks(range(3))
    ax.set_xticklabels(group_labels, fontsize=FONTSIZE_TICK)
    ax.set_yticklabels(["Mean", "Std Dev", "Count"], fontsize=FONTSIZE_TICK)
    
    for i in range(3):
        for j in range(len(group_labels)):
            ax.text(j, i, f"{summary_array[i, j]:.2f}",
                   ha="center", va="center", color="black", fontsize=9, fontweight="bold")
    
    ax.set_facecolor(LIGHT_COLOR)
    ax.set_title("Summary Statistics Heatmap", fontsize=FONTSIZE_HEADING, fontweight="bold", color=DARK_COLOR, pad=12)
    plt.colorbar(im, ax=ax, label="Value")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)


def create_range_plot(group_data, group_names, colors):
    """
    Create a plot showing range, IQR, and median for each group.
    
    Args:
        group_data (dict): Groups with data lists
        group_names (list): List of group names
        colors (list): Colors for groups
        
    Returns:
        BytesIO: Figure as bytes
    """
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#ffffff")
    
    for idx, name in enumerate(group_names):
        data = group_data[name]
        arr = np.array(data)
        q1, median, q3 = np.percentile(arr, [25, 50, 75])
        
        # Plot range
        ax.plot([idx, idx], [arr.min(), arr.max()], "o-",
               color=colors[idx % len(colors)], linewidth=2, markersize=6, alpha=0.6, label=name)
        
        # Plot IQR
        ax.fill_between([idx-0.1, idx+0.1], q1, q3, alpha=0.4, color=colors[idx % len(colors)])
        
        # Plot median
        ax.plot([idx-0.15, idx+0.15], [median, median], "k-", linewidth=2.5)
    
    ax.set_xticks(range(len(group_names)))
    ax.set_xticklabels(group_names, fontsize=FONTSIZE_TICK)
    
    _apply_common_styling(ax, "Range, IQR & Median")
    ax.set_ylabel("Value", fontsize=FONTSIZE_LABEL, color=DARK_COLOR, fontweight="500")
    
    plt.tight_layout()
    return _get_fig_bytes(fig)
