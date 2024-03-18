from heapq import heappop, heappush
from typing import List


class Elements:

    def top_k_frequent_v1(self, nums: List[int], k: int) -> List[int]:
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

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for index in range(len(buckets) - 1, -1, -1):
            if buckets[index]:
                for num in buckets[index]:
                    result.append(num)
                if len(result) == k:
                    break
        return result

    def top_k_frequent_v0(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Heap
        T :O(N log K)
        S: O(N + K)
        :param nums:
        :param k:
        :return:
        """

        if len(nums) == k:
            return nums

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        min_heap = []
        for num, freq in freq_map.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        result = []
        for _, num in min_heap:
            result.append(num)
        return result


if __name__ == "__main__":
    elements = Elements()
    print(elements.top_k_frequent_v0([1, 1, 1, 2, 2, 3, 3, 4], 3))
    print(elements.top_k_frequent_v1([1, 1, 1, 2, 2, 3, 3, 4], 3))
    print(elements.top_k_frequent_v0([1, 1, 1, 2, 2, 3], 2))
    print(elements.top_k_frequent_v1([1, 1, 1, 2, 2, 3], 2))
    print(elements.top_k_frequent_v0([1, 1, 1], 1))
    print(elements.top_k_frequent_v1([1, 1, 1], 1))
