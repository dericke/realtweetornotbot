""" Helper functions for extracting user names out of OCR-read text """

import re

USERNAME_REGEX = r"@[A-Za-z0-9_]{4,15}"


def find_users(text):
    """ Returns all user names found within the total OCR text as list of strings """
    return re.findall(USERNAME_REGEX, text)
