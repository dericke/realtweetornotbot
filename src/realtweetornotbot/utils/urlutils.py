""" Helper functions for URLs """

import requests

IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg", "image/webp")


def is_imgur_url(url):
    """ Returns true, if an image url is an IMGUR image or album """
    return "imgur.com" in url


def is_image_url(url):
    """ Returns true if the url is to an image file """
    try:
        r = requests.head(url)
        if r.headers.get("content-type") in IMAGE_FORMATS:
            return True
    except requests.exceptions.MissingSchema:
        print("Missing Schema Exception")
    return False
