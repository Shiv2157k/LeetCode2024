from typing import List


class ThreeSum:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers
        T: O(N log N + N^2)
        S: O(log n) to O(N)
        :param nums:
        :return:
        """

        if not nums:
            return []

        # sort
        nums.sort()
        result = []

        for index in range(len(nums)):

            # target 0 cannot be generated
            if nums[index] > 0:
                break

            if index == 0 or nums[index] != nums[index - 1]:
                self.twoSum(nums, index, result)
        return result

    def twoSum(self, nums: List[int], preIndex: int, result: List[List[int]]) -> None:

        left = preIndex + 1
        right = len(nums) - 1

        while left < right:

            first, second, third = nums[preIndex], nums[left], nums[right]
            currSum = first + second + third

            if currSum == 0:
                result.append([first, second, third])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif currSum > 0:
                right -= 1
            else:
                left += 1
