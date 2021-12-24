from realtweetornotbot.ocranalysis import ContentProcessor, DateProcessor, ImageProcessor, UserProcessor
from realtweetornotbot.twittersearch import Criteria


class CriteriaBuilder:
    """ Builder for the criteria model """

    @staticmethod
    def image_to_search_criteria_candidates(image_url):
        """ Converts an url to an image of a tweet to a list of possible search criteria """
        ocr_text = ImageProcessor.image_to_text(image_url)
        users_found = UserProcessor.find_users(ocr_text)
        dates_found = DateProcessor.find_dates(ocr_text)
        content_found = ContentProcessor.find_content(ocr_text)
        return CriteriaBuilder.__create_criteria_candidates(
            users_found, dates_found, content_found
        )

    @staticmethod
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
