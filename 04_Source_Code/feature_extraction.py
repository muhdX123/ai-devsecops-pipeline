import re


def extract_features(text):
    """
    Extract simple features from preprocessed input
    for preliminary vulnerability detection.
    """

    text = text.lower()

    features = {
        "contains_sql_keyword": int(
            bool(re.search(r"\b(select|union|insert|update|delete|drop)\b", text))
        ),

        "contains_sql_operator": int(
            bool(re.search(r"('|--|/\*|\*/|;)", text))
        ),

        "contains_script_tag": int(
            bool(re.search(r"<\s*script\b", text))
        ),

        "contains_event_handler": int(
            bool(re.search(r"\bon\w+\s*=", text))
        ),

        "contains_javascript_scheme": int(
            "javascript:" in text
        ),

        "input_length": len(text)
    }

    return features


if __name__ == "__main__":

    sample_inputs = [
        "' OR '1'='1",
        "<script>alert('XSS')</script>",
        "username=admin"
    ]

    for sample in sample_inputs:
        print("Input:", sample)
        print("Features:", extract_features(sample))
        print()
