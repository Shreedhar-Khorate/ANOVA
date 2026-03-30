"""
Configuration & Constants for ANOVA Analysis Tool
"""

# ─── Application Settings ──────────────────────────────────────
APP_TITLE = "ANOVA Analysis Tool"
APP_ICON = "📊"
APP_LAYOUT = "wide"

# ─── Statistical Settings ──────────────────────────────────────
DEFAULT_ALPHA = 0.05
MIN_ALPHA = 0.01
MAX_ALPHA = 0.10
ALPHA_STEP = 0.01

MIN_GROUPS = 2
MAX_GROUPS = 6
DEFAULT_GROUPS = 3

# ─── Color Palette ────────────────────────────────────────────
PRIMARY_COLOR = "#6366f1"
PRIMARY_DARK = "#4f46e5"
PRIMARY_LIGHT = "#818cf8"
SECONDARY_COLOR = "#ec4899"
SUCCESS_COLOR = "#10b981"
DANGER_COLOR = "#ef4444"
WARNING_COLOR = "#f59e0b"
INFO_COLOR = "#3b82f6"
DARK_COLOR = "#1f2937"
LIGHT_COLOR = "#f9fafb"
BORDER_COLOR = "#e5e7eb"
TEXT_COLOR = "#4b5563"

# ─── Color Palette for Groups ─────────────────────────────────
GROUP_COLORS = [
    "#667eea",  # Indigo
    "#ef5350",  # Red
    "#66bb6a",  # Green
    "#ffa726",  # Orange
    "#764ba2",  # Purple
    "#26a69a",  # Teal
]

# ─── Font Families ────────────────────────────────────────────
FONT_POPPINS = "'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
FONT_SPACE_GROTESK = "'Space Grotesk', sans-serif"

# ─── Data Validation ──────────────────────────────────────────
MIN_VALUES_PER_GROUP = 2
MIN_DATA_POINTS_TOTAL = 3

# ─── Visualization Settings ───────────────────────────────────
PLOT_DPI = 100
PLOT_FORMAT = "png"
PLOT_BBOX = "tight"
PLOT_FIGSIZE_SINGLE = (9, 4)
PLOT_FIGSIZE_DOUBLE = (18, 5)
PLOT_FIGSIZE_HEATMAP = (14, 5)

# ─── Grid & Spacing ──────────────────────────────────────────
GRID_ALPHA = 0.1
GRID_LINESTYLE = "--"

# ─── Font Sizes ──────────────────────────────────────────────
FONTSIZE_TITLE = 12
FONTSIZE_HEADING = 11
FONTSIZE_LABEL = 10
FONTSIZE_TICK = 8
FONTSIZE_LEGEND = 8.5

# ─── Effect Size Thresholds ──────────────────────────────────
EFFECT_SIZE_NEGLIGIBLE = 0.01
EFFECT_SIZE_SMALL = 0.06
EFFECT_SIZE_MEDIUM = 0.14

# ─── Report Settings ─────────────────────────────────────────
PDF_ENABLED = True
PDF_PAGESIZE = "letter"
PDF_MARGIN = 0.75  # inches
PDF_DPI = 100

TXT_ENABLED = True
HTML_ENABLED = True

# ─── Sample Dataset Names ──────────────────────────────────────
SAMPLE_DATASET_EXAM = "Student Exam Scores (3 teaching methods)"
SAMPLE_DATASET_YIELD = "Crop Yield (3 fertilizers)"
SAMPLE_DATASET_SIMILAR = "No Significant Difference (similar groups)"
