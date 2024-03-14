from collections import deque


class Logger:

    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()
        self._msg_dict = {}

    def should_print_logger_message(self, message: str, timestamp: int) -> bool:
        """
        Approach: Using Queue and Set
        :param message:
        :param timestamp:
        :return:
        """

        # if there are message in queue
        while self._msg_queue:
            # fetch the first queued element in the queue
            msg, ts = self._msg_queue[0]
            # check the ts is within the range
            if timestamp - ts >= 10:
                # pop the queue and remove this from the set
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break

        # now add new message to set and queue if it does not exists
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False

    def should_print_logger_message_(self, message: str, timestamp: int) -> bool:
        """
        Approach: HashMap
        :param message:
        :param timestamp:
        :return:
        """

        # 1. if it is not in hashmap add and return true

        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True

        # 2. if it is there check the ts is not within range
        #    - if so update and return True
        #    - otherwise return False
        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        else:
            return False


