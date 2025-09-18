import re

def clean_text(text: str) -> str:
    """
    Cleans input text by:
    - Lowercasing
    - Removing URLs
    - Removing mentions (@username)
    - Removing non-alphabet characters
    - Removing extra spaces
    """
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+", "", text)         # remove urls
    text = re.sub(r"@\w+", "", text)            # remove mentions
    text = re.sub(r"[^a-z\s]", "", text)        # keep only letters
    text = re.sub(r"\s+", " ", text).strip()    # remove extra spaces
    return text