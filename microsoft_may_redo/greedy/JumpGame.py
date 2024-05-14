from typing import List


class JumpGame:

    def can_jump(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        max_reach = 0
        length = len(nums)

        for index in range(len(nums)):
            if max_reach < index + nums[index]:
                max_reach = index + nums[index]

            if max_reach == index:
                break
        return max_reach >= length - 1
