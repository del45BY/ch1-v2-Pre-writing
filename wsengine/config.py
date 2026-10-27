"""Brand, palette, fonts, template definitions and category wording.

Everything visual or textual that is NOT row data lives here, so a re-brand
or a new template never touches the rendering code.
"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
IMAGE_DIR = ROOT / "assets" / "images"  # optional PNG artwork named {slug}.png
OUTPUT_DIR = ROOT / "PRODUCTS"

# ------------------------------------------------------------------ brand
BRAND = {
    "name": "Sleepless Learning",
    "tagline": "Preschool Educational Series",
    "copyright": "\u00a9 2026 Preschool Digital Education Series. For personal and classroom use only. Do not resell or redistribute.",
}

# ------------------------------------------------------------------ page
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt, portrait
MARGIN = 34
CONTENT_TOP = PAGE_H - 152  # just below the header module
CONTENT_BOTTOM = 100  # just above parent tip + footer

# ------------------------------------------------------------------ palette
NAVY, GREY, LIGHT, LINE = "#2B2D42", "#6B7280", "#F4F9FF", "#C9D6EA"
TEMPLATE_COLORS = {
    "A": "#4D9DE0", "B": "#3FB984", "C": "#F59E0B", "D": "#EC6A9B", "E": "#8B7CF6",
    "F": "#14B8A6", "G": "#EF4444", "H": "#6366F1", "I": "#84CC16", "J": "#F97316",
    "K": "#0EA5E9", "L": "#D946EF", "M": "#10B981", "N": "#E11D48", "O": "#7C3AED",
    "P": "#EAB308", "Q": "#06B6D4", "R": "#F43F5E", "S": "#22C55E", "T": "#2563EB",
}
SWATCHES = ["#FF595E", "#FFB703", "#FFD23F", "#6BCB77", "#4D9DE0", "#8B7CF6", "#C68642"]

# ------------------------------------------------------------------ fonts
_FONT_DIRS = [
    ROOT / "assets" / "fonts",
    Path("C:/Windows/Fonts"),
    Path("/usr/share/fonts/truetype/google-fonts"),
    Path("/usr/share/fonts/truetype/noto"),
]


def _register(name: str, filename: str, fallback: str) -> str:
    for d in _FONT_DIRS:
        p = d / filename
        if p.exists():
            pdfmetrics.registerFont(TTFont(name, str(p)))
            return name
    return fallback


# Fonts Standard (Latin)
F_BOLD = _register("Brand-Bold", "Poppins-Bold.ttf", "Helvetica-Bold")
F_MED = _register("Brand-Medium", "Poppins-Medium.ttf", "Helvetica")
F_REG = _register("Brand-Regular", "Poppins-Regular.ttf", "Helvetica")
F_IT = _register("Brand-Italic", "Poppins-Italic.ttf", "Helvetica-Oblique")

# Fonts CJK (Jepang/Mandarin) & RTL (Arab)
F_JA_REG = _register("Brand-JA-Regular", "NotoSansJP-Regular.ttf", F_REG)
F_JA_BOLD = _register("Brand-JA-Bold", "NotoSansJP-Bold.ttf", F_BOLD)
F_AR_REG = _register("Brand-AR-Regular", "NotoNaskhArabic-Regular.ttf", F_REG)
F_AR_BOLD = _register("Brand-AR-Bold", "NotoNaskhArabic-Bold.ttf", F_BOLD)


def get_font_for_lang(lang: str, is_bold: bool = False) -> str:
    """Mengembalikan font yang sesuai berdasarkan kode bahasa."""
    lang = lang.lower()
    if lang in ("ja", "zh"):
        return F_JA_BOLD if is_bold else F_JA_REG
    elif lang == "ar":
        return F_AR_BOLD if is_bold else F_AR_REG
    return F_BOLD if is_bold else F_REG


FONT_FILE_BOLD = next(
    (str(d / "Poppins-Bold.ttf") for d in _FONT_DIRS if (d / "Poppins-Bold.ttf").exists()), None
)
FONT_FILE_MED = next(
    (str(d / "Poppins-Medium.ttf") for d in _FONT_DIRS if (d / "Poppins-Medium.ttf").exists()), None
)

# ------------------------------------------------------------------ template registry (Keys Only)
TEMPLATES = {
    "A": dict(name="Animal Matching", activity="Matching", key="template_a"),
    "B": dict(name="Vocabulary Learning", activity="Tracing", key="template_b"),
    "C": dict(name="Find and Circle", activity="Circle the correct answer", key="template_c"),
    "D": dict(name="Cut and Paste", activity="Cutting and pasting", key="template_d"),
    "E": dict(name="Coloring Worksheet", activity="Coloring", key="template_e"),
}
TEMPLATE_ORDER = ["A", "B", "C", "D", "E"]


# ------------------------------------------------------------------ PRE-WRITING SERIES (A-J)
SERIES_PREWRITE = "Pra-Menulis & Motorik Halus"

PREWRITE_TEMPLATES = {
    "A": dict(name="Vertical Lines", activity="Vertical line tracing", key="prewrite_a", series=SERIES_PREWRITE),
    "B": dict(name="Horizontal Lines", activity="Horizontal line tracing", key="prewrite_b", series=SERIES_PREWRITE),
    "C": dict(name="Diagonal Lines", activity="Diagonal line tracing", key="prewrite_c", series=SERIES_PREWRITE),
    "D": dict(name="Zigzag Lines", activity="Zigzag line tracing", key="prewrite_d", series=SERIES_PREWRITE),
    "E": dict(name="Curved Lines", activity="Curved line tracing", key="prewrite_e", series=SERIES_PREWRITE),
    "F": dict(name="Wavy Lines", activity="Wavy line tracing", key="prewrite_f", series=SERIES_PREWRITE),
    "G": dict(name="Circles & Spirals", activity="Circle and spiral tracing", key="prewrite_g", series=SERIES_PREWRITE),
    "H": dict(name="Mixed Patterns", activity="Pattern continuing", key="prewrite_h", series=SERIES_PREWRITE),
    "I": dict(name="Path Tracing", activity="Path tracing", key="prewrite_i", series=SERIES_PREWRITE),
    "J": dict(name="Shape Tracing", activity="Basic shape tracing", key="prewrite_j", series=SERIES_PREWRITE),
}

# Object pairs mapping (Word IDs)
PREWRITE_CONTENT = {
    "B": [("lebah", "madu"), ("kelinci", "wortel"), ("ikan", "ombak"), ("burung", "rumah")],
    "D": [("gajah", "jeruk"), ("babi", "apel"), ("bebek", "kapal")],
    "E": [("bola", "bintang")],
    "F": [("bebek", "ombak"), ("ular", "hati"), ("ikan", "kapal")],
    "I": [("lebah", "madu"), ("kelinci", "wortel"), ("ikan", "ombak"), ("babi", "rumah")],
}

PREWRITE_SET = dict(
    order=list("ABCDEFGHIJ"),
    category="Pre-Writing",
    folder="Pre-Writing and Fine Motor Skills A-J",
    i18n_key="prewrite_set",
)