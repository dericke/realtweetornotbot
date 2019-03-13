from queue import Queue
from queue import Empty
from threading import Thread, Lock
from utils import Logger

PRODUCER_THREAD_COUNT = 20
CONSUMER_THREAD_COUNT = 1

post_queue = Queue()
result_queue = Queue()
bot_interface = None
threads = []


class MultiThreadSearcher:
    """ Multi-threading scheduler for the bot """

    tesseract_lock = Lock()

    @staticmethod
    def init(bot_interface_impl):
        """ Initialises the scheduler with the bot """
        global bot_interface
        bot_interface = bot_interface_impl
        Logger.log_dispatching_threads(PRODUCER_THREAD_COUNT, CONSUMER_THREAD_COUNT)

        for i in range(0, PRODUCER_THREAD_COUNT):
            t = ProducerThread()
            threads.append(t)
            t.start()

        for i in range(0, CONSUMER_THREAD_COUNT):
            t = ConsumerThread()
            threads.append(t)
            t.start()

    @staticmethod
    def start():
        global bot_interface
        global post_queue
        global result_queue

        new_posts = bot_interface.fetch_new_posts()
        for new_post in new_posts:
            post_queue.put(new_post)

        post_queue.join()
        result_queue.join()
        MultiThreadSearcher.stop()

    @staticmethod
    def stop():
        for thread in threads:
            thread.stopped = True


class ProducerThread(Thread):
    stopped = False

    def run(self):
        global post_queue
        global bot_interface

        while not self.stopped:
            try:
                post = post_queue.get_nowait()
                tweets = bot_interface.find_tweet(post)
                result_queue.put((post, tweets))
                post_queue.task_done()
            except Empty:
                pass


class ConsumerThread(Thread):
    stopped = False

    def run(self):
        global result_queue
        global bot_interface

        while not self.stopped:
            try:
                result = result_queue.get_nowait()
                bot_interface.handle_tweet_result(result[0], result[1])
                result_queue.task_done()
            except Empty:
                pass
