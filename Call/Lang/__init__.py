"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

import json
import os

LANG_DIR = os.path.dirname(__file__)
DEFAULT_LANG = "en"

# Load all language files
langs = {}
for file in os.listdir(LANG_DIR):
    if file.endswith(".json"):
        with open(os.path.join(LANG_DIR, file), encoding="utf-8") as f:
            langs[file.replace(".json", "")] = json.load(f)

def get_string(lang_code, key):
    lang = langs.get(lang_code, langs[DEFAULT_LANG])
    return lang.get(key, key)
  
