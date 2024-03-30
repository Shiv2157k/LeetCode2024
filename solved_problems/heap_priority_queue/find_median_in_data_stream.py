import heapq


class DataStream:

    # other approaches include sorting the list in median method
    # performing insertion sort using binary search
    # Building a BST Tree - odd root will be median
    # otherwise I guess we need to pick right/ left node val

    def __init__(self):
        # store min elements
        self._max_heap = []
        # store max elements
        self._min_heap = []

    def add(self, num: float):

        heapq.heappush(self._max_heap, -num)
        heapq.heappush(self._min_heap, -heapq.heappop(self._max_heap))
        if len(self._max_heap) < len(self._min_heap):
            heapq.heappush(self._min_heap, -heapq.heappop(self._max_heap))

    def get_median(self) -> float:

        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]
        else:
            return float(-self._max_heap[0] + self._min_heap[0]) / 2