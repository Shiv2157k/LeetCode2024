from heapq import heappop, heappush
from typing import List


class FrequentElements:

    def topKV1(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Bucket Sorting
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """
        if len(nums) == k:
            return nums

        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            bucket[freq].append(num)

        result = []
        for freq in range(len(bucket) - 1, -1, -1):
            if bucket[freq]:
                for num in bucket[freq]:
                    result.append(num)
                    if len(result) == k:
                        return result
        return result

    def topKV0(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Heap
        T: O(N log K)
        S: O(N + K)
        :param nums:
        :return:
        """
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        minHeap = []

        for num, freq in freqMap.items():
            heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heappop(minHeap)
        result = []
        while minHeap:
            _, num = heappop(minHeap)
            result.append(num)
        return result


if __name__ == "__main__":
    freqElements = FrequentElements()
    print(freqElements.topKV0([1, 1, 1, 2, 2, 3], 2))
    print(freqElements.topKV0([1], 1))

    print(freqElements.topKV1([1, 1, 1, 2, 2, 3], 2))
    print(freqElements.topKV1([1], 1))
