from collections import deque
from typing import List


class RLEIterator:

    def __init__(self, encodedList: List[int]):
        self.queue = deque(encodedList)

    def next(self, n):

        while self.queue and n > self.queue[0]:
            n -= self.queue[0]
            self.queue.popleft()
            self.queue.popleft()
        if self.queue and n <= self.queue[0]:
            self.queue[0] -= n
            return self.queue[1]
        return -1


if __name__ == "__main__":
    rle_iterator = RLEIterator([3, 8, 0, 9, 2, 5])
    print(rle_iterator.next(2))
    print(rle_iterator.next(2))
    print(rle_iterator.next(1))
    print(rle_iterator.next(1))
