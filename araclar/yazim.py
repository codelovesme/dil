"""Türk dillerinin yazılarını çalışma yazımına (ILKELER §11) aktarır.

calisma(kod, metin) -> küçük harfli, noktalamasız, çalışma yazımında metin.
Kiril, Latin ve Uygur (Arap) yazıları desteklenir. Osmanlıca Arap yazısı
ünlüleri göstermediği için aktarılmaz (olduğu gibi döner).

Bu aktarım ölçüm içindir: iki metni aynı yazıda karşılaştırmak. Sözlükteki
biçimlerin yazımı kaynağa göre elle denetlenir.
"""
from __future__ import annotations

import re
import unicodedata

KIRIL = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "j", "з": "z",
         "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
         "с": "s", "т": "t", "у": "u", "ф": "f", "х": "x", "ц": "ts", "ч": "ç", "ш": "ş", "щ": "şç",
         "ъ": "", "ы": "ı", "ь": "", "э": "e", "ю": "yu", "я": "ya", "ә": "ä", "ө": "ö", "ү": "ü",
         "ң": "ñ", "ҥ": "ñ", "ҡ": "k", "қ": "k", "ғ": "ğ", "ҕ": "ğ", "ҙ": "z", "һ": "h", "ұ": "u",
         "і": "i", "ӧ": "ö", "ӱ": "ü", "ј": "y", "ӑ": "ă", "ӗ": "ĕ", "ӳ": "ü", "ҫ": "ş", "ҷ": "c",
         "ӌ": "c", "ӄ": "k", "ӈ": "ñ", "җ": "c", "ў": "ö", "ҳ": "h", "ҝ": "g", "ҹ": "c"}
KIRIL_OZEL = {
    "bak": [("ҫ", "s")],
    "krc": [("дж", "c"), ("нг", "ñ"), ("гъ", "ğ"), ("къ", "k")],
    "kum": [("гъ", "ğ"), ("къ", "k"), ("нг", "ñ"), ("оь", "ö"), ("уь", "ü")],
    "nog": [("оь", "ö"), ("уь", "ü"), ("нъ", "ñ"), ("къ", "k"), ("гъ", "ğ")],
    "sah": [("дь", "c"), ("нь", "ny")], "dlg": [("дь", "c"), ("нь", "ny")], "alt": [("дь", "c")],
}
LATIN_OZEL = {
    "tuk": [("y", "\0"), ("ý", "y"), ("\0", "ı"), ("ň", "ñ"), ("ž", "j")],
    "uzb": [("o‘", "ö"), ("o'", "ö"), ("oʻ", "ö"), ("o’", "ö"), ("g‘", "ğ"), ("g'", "ğ"), ("gʻ", "ğ"),
            ("g’", "ğ"), ("sh", "ş"), ("ch", "ç"), ("ng", "ñ"), ("q", "k")],
    "aze": [("ə", "ä"), ("q", "k")],
    "crh": [("q", "k")], "tat": [("q", "k")], "krc": [("q", "k")], "kaz": [("q", "k")],
    "kaa": [("á", "ä"), ("ó", "ö"), ("ú", "ü"), ("ń", "ñ"), ("ǵ", "ğ"), ("q", "k")],
}
UYGUR = {"ا": "a", "ە": "ä", "ب": "b", "پ": "p", "ت": "t", "ج": "c", "چ": "ç", "خ": "x", "د": "d",
         "ر": "r", "ز": "z", "ژ": "j", "س": "s", "ش": "ş", "غ": "ğ", "ف": "f", "ق": "k", "ك": "k",
         "گ": "g", "ڭ": "ñ", "ل": "l", "م": "m", "ن": "n", "ھ": "h", "و": "o", "ۇ": "u", "ۆ": "ö",
         "ۈ": "ü", "ۋ": "v", "ې": "e", "ى": "i", "ي": "y", "ئ": "", "ـ": ""}

_KIRIL_RX = re.compile("[Ѐ-ӿ]")
_ARAP_RX = re.compile("[؀-ۿ]")


def _kiril(kod: str, s: str) -> str:
    for a, b in KIRIL_OZEL.get(kod, []):
        s = s.replace(a, b)
    s = re.sub(r"(^|[\s\-])е", r"\1ye", s)          # söz başında е = ye
    return "".join(KIRIL.get(ch, ch) for ch in s)


def _latin(kod: str, s: str) -> str:
    for a, b in LATIN_OZEL.get(kod, []):
        s = s.replace(a, b)
    return s


def calisma(kod: str, metin: str) -> str:
    s = unicodedata.normalize("NFC", metin).lower().replace("İ".lower(), "i")
    if _ARAP_RX.search(s):
        if kod == "uig":
            s = "".join(UYGUR.get(ch, ch) for ch in s)
        else:
            return s
    elif _KIRIL_RX.search(s):
        s = _kiril(kod, s)
    else:
        s = _latin(kod, s)
    s = s.replace("’", "").replace("'", "").replace("ʼ", "")
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()
