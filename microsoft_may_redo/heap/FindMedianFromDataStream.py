from heapq import heappop, heappush


class FindMedianFromDataStream:

    def __init__(self):
        # max heap
        self.__small_heap = []
        # min heap
        self.__large_heap = []

    def add_num(self, num: int) -> None:

        heappush(self.__small_heap, -num)

        # case 1: if val in small heap > large heap
        if self.__small_heap and self.__large_heap and -self.__small_heap[0] > self.__large_heap[0]:
            val = -heappop(self.__small_heap)
            heappush(self.__large_heap, val)

        # case 2: diff in heap size is greater than one or uneven
        if len(self.__small_heap) > len(self.__large_heap) + 1:
            val = -heappop(self.__small_heap)
            heappush(self.__large_heap, val)

        if len(self.__large_heap) > len(self.__small_heap) + 1:
            val = heappop(self.__large_heap)
            heappush(self.__small_heap, -val)

    def find_median(self) -> float:

        if len(self.__small_heap) > len(self.__large_heap):
            return -self.__small_heap[0]

        if len(self.__large_heap) > len(self.__small_heap):
            return self.__large_heap[0]

        return (-self.__small_heap[0] + self.__large_heap[0]) / 2
