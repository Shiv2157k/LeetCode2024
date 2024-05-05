from typing import List


class NextGreaterElement:

    def next_greater_elements(self, nums: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        stack: List[int] = []
        result: List[int] = [-1] * len(nums)

        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    result[stack.pop()] = num
                stack.append(i)
        return result
