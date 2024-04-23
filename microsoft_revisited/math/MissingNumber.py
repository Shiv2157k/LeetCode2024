from typing import List


class MissingNumbers:

    def missing_number(self, nums: List[int]) -> int:
        """
        Approach: Cumulative Sum
        T: O(M)
        S: O(1)
        :param nums:
        :return:
        """

        # since it will be range from 1 - n
        # for example [1, 2, 3] -> expected: 1 + 2 + 3 = 6
        # say given is [1, 0, 3] -> expected - currSum = ans
        # formula: n * (n + 1) // 2 = 3 * (3 + 1) // 2 => 12 // 2 = 6
        n = len(nums)
        expected_sum = n * ((n + 1) // 2)
        curr_sum = 0
        for num in nums:
            curr_sum += num
        return expected_sum - curr_sum
