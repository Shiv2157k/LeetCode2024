from typing import List


class ThreeSumClosest:

    def getClosestNumber(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        T: O(N^2)
        S: O(N)
        :return:
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        diff = float("inf")

        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[index] + nums[left] + nums[right]
                if abs(target - currentSum) < abs(diff):
                    diff = target - currentSum
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break
        return target - diff


if __name__ == "__main__":
    threeSumClosest = ThreeSumClosest()
    print(threeSumClosest.getClosestNumber([-1, 2, 1, -4], 1))
    print(threeSumClosest.getClosestNumber([0, 0, 0], 1))
