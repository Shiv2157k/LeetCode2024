from typing import List


class ThreeSumClosest:


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointer
        T: O(N^2)
        S: O(log N) or O(N)
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        diff = float('inf')

        for index in range(len(nums)):

            left = index + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[index] + nums[left] + nums[right]

                if abs(target - currSum) < abs(diff):
                    diff = target - currSum
                elif currSum < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break
        return target - diff