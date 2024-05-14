from typing import List


class NextGreaterElement:

    def next_greater_element(self, nums: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O (N)
        :param nums:
        :return:
        """

        stack = []
        result = [-1] * len(nums)
        for _ in range(2):
            for i in range(len(nums)):

                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                stack.append(i)
        return result

    def next_greater_element(self, nums: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        stack = []
        result = [-1] * len(nums)

        for i in range(2 * len(nums) - 1, -1, -1):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            result[i % len(nums)] = nums[stack[-1]] if stack else -1
            stack.append(i % len(nums))
        return result
