import re
from urllib.parse import unquote


def preprocess_input(text):
    """
    Clean and normalize source code or HTTP request input
    before feature extraction and vulnerability detection.
    """

    if not isinstance(text, str):
        text = str(text)

    # Decode URL-encoded characters
    text = unquote(text)

    # Remove unnecessary spaces
    text = text.strip()

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    return text


if __name__ == "__main__":

    sample_inputs = [
        "' OR '1'='1",
        "<script>alert('XSS')</script>"
    ]

    for sample in sample_inputs:
        print("Original :", sample)
        print("Processed:", preprocess_input(sample))
        print()
