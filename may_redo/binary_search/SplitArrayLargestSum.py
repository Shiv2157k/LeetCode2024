from typing import List


class SplitArrayLargestSum:

    def split_array(self, nums: List[int], m: int) -> int:
        """
        Approach:
        T: O(N * log S)
        S: O(1)
        :param nums:
        :param m:
        :return:
        """

        def can_split(largest: int):

            sub_array = 0
            curr_sum = 0

            for n in nums:
                curr_sum += n
                if curr_sum > largest:
                    sub_array += 1
                    curr_sum = n
            return sub_array + 1 <= m

        left = max(nums)
        right = sum(nums)

        result = right

        while left <= right:
            pivot = left + (right - left) // 2

            if can_split(pivot):
                result = pivot
                right = pivot - 1
            else:
                left = pivot + 1
        return result
