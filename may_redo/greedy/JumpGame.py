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
        max_jump = 0

        for i in range(len(nums)):
            if max_jump < i + nums[i]:
                max_jump = i + nums[i]
            if max_jump == i:
                break
        return max_jump >= len(nums) - 1
