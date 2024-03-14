import heapq
from typing import List
from collections import Counter


class Subsequence:

    def find_subsequence_with_k_largest_sum(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Sort
        TC: n * log N
        SC: O(M)
        :param nums:
        :param k:
        :return:
        """
        val_and_index = sorted([num, i] for i, num in enumerate(nums))
        return [num for num, i in sorted(val_and_index[-k:], key=lambda x: x[1])]

    def find_subsequence_with_k_largest_sum_(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Heap / map Two Pass
        TC: n * log N
        SC: O(M)
        :param nums:
        :param k:
        :return:
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        occurrences = Counter(heap)

        result = []
        for num in nums:
            if occurrences[num] > 0:
                occurrences[num] -= 1
                result.append(num)
        return result

    def find_subsequence_with_k_largest_sum___(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Heap / map One Pass
        TC: n * log N
        SC: O(M)
        :param nums:
        :param k:
        :return:
        """
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [h[0] for h in sorted(heap, key=lambda x: x[1])]

    def find_subsequence_with_k_largest_sum__(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Quick Select Algorithm
        :param nums:
        :param k:
        :return:
        """

        def quickSelect(lo: int, hi: int) -> int:
            pivot = index[lo]
            while lo < hi:
                while lo < hi and nums[index[hi]] <= nums[pivot]:
                    hi -= 1
                index[lo] = index[hi]
                while lo < hi and nums[index[lo]] >= nums[pivot]:
                    lo += 1
                index[hi] = index[lo]
            index[lo] = pivot
            return lo

        n = len(nums)
        left, right = 0, n - 1
        index = list(range(n))

        while left < right:
            idx = quickSelect(left, right)
            if idx < k:
                left = idx + 1
            else:
                right = idx

        kth_val, freq_of_kth_val = nums[index[k - 1]], 0
        for i in index[:k]:
            if nums[i] == kth_val:
                freq_of_kth_val += 1

        seq = []
        for num in nums:
            if num > kth_val or num == kth_val and freq_of_kth_val > 0:
                seq.append(num)
                if num == kth_val:
                    freq_of_kth_val -= 1
        return seq


if __name__ == "__main__":

    subsequence = Subsequence()
    print(subsequence.find_subsequence_with_k_largest_sum__([3, 1, 4, 1, 7, 5, 9, 2, 6, 5, 3, 5],4))
    print(subsequence.find_subsequence_with_k_largest_sum([3, 1, 4, 1, 7, 5, 9, 2, 6, 5, 3, 5],4))
    print(subsequence.find_subsequence_with_k_largest_sum___([3, 1, 4, 1, 7, 5, 9, 2, 6, 5, 3, 5],4))
    print(subsequence.find_subsequence_with_k_largest_sum_([3, 1, 4, 1, 7, 5, 9, 2, 6, 5, 3, 5],4))



