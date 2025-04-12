import re
from apostrophe_dict import APOSTROPHE_DICT

def expand_contractions(text):
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, APOSTROPHE_DICT.keys())) + r')\b')
    return pattern.sub(lambda match: APOSTROPHE_DICT[match.group(0)], text)

def normalize_text(text):
    text = text.lower()
    text = expand_contractions(text)
    return text
