from heapq import heappop, heappush


class MedianFromADataStream:

    def __init__(self):
        # large heap -> min heap
        self._large = []
        # small heap -> max heap
        self._small = []

    def add(self, num: int):

        heappush(self._small, -1 * num)

        # make sure every in small <= every num in large
        # i.e., if small[0] > large[0] move the small to large
        # order difference
        if self._large and self._small and (-self._small[0] > self._large[0]):
            val = -heappop(self._small)
            heappush(self._large, val)

        # uneven size
        if len(self._small) > len(self._large) + 1:
            val = -heappop(self._small)
            heappush(self._large, val)

        if len(self._large) > len(self._small) + 1:
            val = heappop(self._large)
            heappush(self._small, -val)

    def find_median(self) -> float:

        if len(self._small) > len(self._large):
            return -self._small[0]
        if len(self._large) > len(self._small):
            return self._large[0]

        return (-self._small[0] + self._large[0]) / 2
