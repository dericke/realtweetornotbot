""" Helper functions for Logging to the console """

import threading


def log_fetch_count(fetch_count):
    """ Logs the amount of posts that have been fetched """
    print(f"<FETCHED POSTS> {fetch_count} new posts. Dispatching workers!\n")


def log_summon_count(fetch_count):
    """ Logs the amount of comment mentions that have been fetched """
    print(f"<FETCHED SUMMONS> {fetch_count} new summons. Dispatching workers!\n")


def log_tweet_found(post_id, image_url):
    """ Logs that a tweet to a given post_id has been found """
    print(f"<WORKER-{threading.currentThread().getName()} - FOUND TWEET>\nPost: https://www.reddit.com/{post_id}\nTweet: {image_url}\n")


def log_no_results(post_id, image_url):
    """ Logs that a worker has not found any tweet result for a given post_id """
    print(f"<WORKER-{threading.currentThread().getName()} - NO RESULTS>\nPost: https://www.reddit.com/{post_id}\nImage: {image_url}\n")


def log_error():
    """ Logs and error in the main loop """
    print("[ERROR OCCURED] --> Sent PM with stacktrace!\n")


def log_error_stacktrace(error_string):
    """ Logs and error with the given stacktrace """
    print(f"[EXCEPTION THROWN]\n{error_string}\n")


def log_db_deletion(delete_count):
    """ Logs the deletion of rows inside the Database """
    print(f"DB >>> Deleting last {delete_count} submission IDs\n")


def log_db_summary_deletion():
    """ Logs the deletion of a summary inside the Database """
    print("DB >>> Deleting last summary\n")


def log_dispatching_threads(producer_count, consumer_count):
    """ Logs the dispatching of worker threads """
    print(f"<MAIN THREAD> Starting: Producers ({producer_count}) and Consumers ({consumer_count})\n")


def log_summary_time(timedelta):
    """ Logs the time difference between now and the last summary time """
    print(f"<MAIN THREAD> Time Diff to last summary: {timedelta}")
