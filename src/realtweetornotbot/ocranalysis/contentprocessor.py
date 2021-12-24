""" Helper functions for extracting a tweet's content out of OCR-read text """

import re


CONTENT_REGEX = r"[^a-zA-Z0-9]"


def find_content(text):
    """ Returns the tweet's content within the total OCR text as string"""
    content = re.sub('[^A-Za-z \n]+', ' ', text)                                          # Remove all special signs
    content = re.sub('\n+', ' ', content)                                                 # Replace newline by space
    content = re.sub(' +', ' ', content)                                                  # Strip multiple spaces
    content = " ".join(w for w in content.split() if len(w) > 1)                          # Remove single letters
    longest_40_words = set(sorted(content.split(), key=lambda x: len(x), reverse=True)[:40])
    content = " ".join(w for w in content.split() if w in longest_40_words)               # Remove short words
    return content
