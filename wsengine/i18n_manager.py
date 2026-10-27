from __future__ import annotations

import importlib
from typing import Any

DEFAULT_LANG = "en"

class I18nManager:
    def __init__(self, target_lang: str = "es"):
        self.target_lang = target_lang.lower()
        self.translations = self._load_lang(self.target_lang)
        self.en_translations = self._load_lang("en")

    def _load_lang(self, lang_code: str) -> dict[str, Any]:
        try:
            module = importlib.import_module(f".i18n.{lang_code}", package=__package__ or "")
            return getattr(module, "TRANSLATIONS", {})
        except ImportError:
            print(f"Warning: Language '{lang_code}' not found. Falling back to English.")
            return {}

    def t(self, key_path: str) -> tuple[str, str]:
        """
        Mengembalikan tuple (target_text, english_text) untuk rendering bilingual.
        Example key_path: 'page_a.sec_1'
        """
        keys = key_path.split(".")
        
        target_val = self.translations
        en_val = self.en_translations
        
        for k in keys:
            target_val = target_val.get(k, {}) if isinstance(target_val, dict) else {}
            en_val = en_val.get(k, {}) if isinstance(en_val, dict) else {}

        target_str = target_val if isinstance(target_val, str) else key_path
        en_str = en_val if isinstance(en_val, str) else key_path
        
        return target_str, en_str