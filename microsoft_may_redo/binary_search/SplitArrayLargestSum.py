from typing import List


class SplitArrayLargestSum:

    def split_array(self, nums: List[int], k: int) -> int:
        """
        Approach: Binary Search
        T: O(N log S)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """

        def can_split(curr_largest: int) -> bool:
            curr_sum = 0
            sub_array = 0

            for num in nums:
                curr_sum += num

                if curr_sum > curr_largest:
                    sub_array += 1
                    curr_sum = num
            return sub_array + 1 <= k

        left = max(nums)
        right = sum(nums)
        result = right

        while left <= right:
            pivot = left + (right - left) // 2

            if can_split(pivot):
                result = min(result, pivot)
                right = pivot - 1
            else:
                left = pivot + 1
        return right
