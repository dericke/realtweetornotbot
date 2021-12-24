""" Builder for the criteria model """

from realtweetornotbot.ocranalysis import (contentprocessor, dateprocessor,
                                           imageprocessor, userprocessor)
from realtweetornotbot.twittersearch import Criteria


def image_to_search_criteria_candidates(image_url):
    """ Converts an url to an image of a tweet to a list of possible search criteria """
    ocr_text = imageprocessor.image_to_text(image_url)
    users_found = userprocessor.find_users(ocr_text)
    dates_found = dateprocessor.find_dates(ocr_text)
    content_found = contentprocessor.find_content(ocr_text)
    return __create_criteria_candidates(
        users_found, dates_found, content_found
    )


def __create_criteria_candidates(found_users, found_dates, content):
    candidates = []

    if not found_users:
        return []

    if not found_dates:
        found_dates.append(None)

    for user in found_users:
        for date in found_dates:
            candidates.append(Criteria(user=user, date=date, content=content))

    return candidates
