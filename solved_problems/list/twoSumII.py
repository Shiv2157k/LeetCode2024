from typing import List


class TwoSumII:

    def get_two_indices(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        left, right = 0, len(nums) - 1

        while left < right:

            result = nums[left] + nums[right]
            if target == result:
                return [left + 1, right + 1]
            elif target < result:
                left += 1
            else:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    two_sum_ii = TwoSumII()
    print(two_sum_ii.get_two_indices([2, 3, 4, 5, 7], 9))
    print(two_sum_ii.get_two_indices([2, 3, 4, 5, 7], 19))