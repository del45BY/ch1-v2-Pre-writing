"""Batch Export Test Suite for Multi-Language Worksheet Generation."""
from __future__ import annotations

import sys
import time
from pathlib import Path

# Fix module import path automatically
CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent if CURRENT_DIR.name == "wsengine" else CURRENT_DIR

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Import database module & config safely
try:
    from wsengine.database import load_words
    from wsengine import config as cfg
except ImportError:
    from database import load_words
    import config as cfg

try:
    from wsengine.i18n_manager import I18nManager
    from wsengine.prewriting import PREWRITE_FUNCS, PrewriteCtx
except ImportError:
    from i18n_manager import I18nManager
    from prewriting import PREWRITE_FUNCS, PrewriteCtx

from reportlab.pdfgen import canvas

ALL_LANGUAGES = ["id", "en", "es", "fr", "de", "pt", "ja", "ar"]
TEMPLATES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
OUTPUT_DIR = ROOT_DIR / "test_output"

# Path ke file Excel database
DB_PATH = cfg.DATA_DIR / "worksheet_database.xlsx"


def run_batch_export_test():
    print("==================================================")
    print("  RUNNING MULTI-LANGUAGE PDF EXPORT TEST (8 LANGS)")
    print("==================================================")
    
    start_time = time.time()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Load words database dengan path wajib
    words_db = {}
    try:
        print(f"[➔] Loading database from: {DB_PATH}")
        words_db = load_words(DB_PATH)
        print(f"[✔] Loaded {len(words_db)} words from database.")
    except Exception as e:
        print(f"[!] Critical Error: Failed to load database at {DB_PATH}: {e}")
        return

    success_count = 0
    fail_count = 0

    # 2. Loop through all supported languages
    for lang in ALL_LANGUAGES:
        lang_upper = lang.upper()
        pdf_path = OUTPUT_DIR / f"PreWriting_Series_{lang_upper}.pdf"
        
        print(f"\n[➔] Processing [{lang_upper}]...")
        
        try:
            c = canvas.Canvas(str(pdf_path))
            
            for idx, t in enumerate(TEMPLATES, start=1):
                ctx = PrewriteCtx(
                    template=t,
                    page_no=idx,
                    page_total=len(TEMPLATES),
                    words=words_db,
                    lang=lang
                )
                
                # Render page
                PREWRITE_FUNCS[t](c, ctx)
                c.showPage()
                
            c.save()
            print(f"    [✔] Successfully generated: {pdf_path.name}")
            success_count += 1
            
        except Exception as err:
            print(f"    [✘] Failed to generate [{lang_upper}]: {err}")
            import traceback
            traceback.print_exc()
            fail_count += 1

    elapsed = time.time() - start_time
    print("\n==================================================")
    print(f"  TEST RESULTS SUMMARY")
    print("==================================================")
    print(f"  Total Languages Attempted : {len(ALL_LANGUAGES)}")
    print(f"  Passed                    : {success_count}")
    print(f"  Failed                    : {fail_count}")
    print(f"  Execution Time            : {elapsed:.2f} seconds")
    print(f"  Output Directory          : {OUTPUT_DIR.resolve()}")
    print("==================================================")


if __name__ == "__main__":
    run_batch_export_test()