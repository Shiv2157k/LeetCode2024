from typing import List, Dict
from heapq import heappop, heappush


class FrequentElements:

    def top_k_v1(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Bucket Sort
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        if len(nums) == k:
            return nums

        # build the frequency table of nums
        num_freq: Dict[int, int] = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        # build a freq bucket and add the elements based on the frequency
        # our bucket will range from 0 to len(nums) in the nums list
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in num_freq.items():
            bucket[freq].append(num)

        # add the numbers in top k
        top_k: List[int] = []
        for freq in range(len(bucket) - 1, -1, -1):
            if len(bucket[freq]) != 0:
                for num in bucket[freq]:
                    top_k.append(num)
                    if len(top_k) == k:
                        return top_k
        return top_k

    def top_k_v0(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Heap
        T: O(N log N)
        S: O(K)
        :param nums:
        :param k:
        :return:
        """

        if k == len(nums):
            return nums

        num_freq: Dict[int, int] = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        min_heap: List[int] = []
        for num, freq in num_freq.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        top_k: List[int] = []
        while min_heap:
            _, num = heappop(min_heap)
            top_k.append(num)
        return top_k  # heapq.nlargest(k, count.keys(), key=count.get)

