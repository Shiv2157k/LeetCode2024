from typing import List


class ThreeSumSmaller:

    def numberOfTripletsSmallerToTarget(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointer
        T: O(N^2)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        totalSmallerTriplets = 0
        nums.sort()

        for index in range(len(nums)):
            totalSmallerTriplets += self._twoSumSmaller(nums, index, target)

        return totalSmallerTriplets

    def _twoSumSmaller(self, nums: List[int], preIndex: int, target: int) -> int:

        left, right = preIndex + 1, len(nums) - 1
        totalSmallerTriplets = 0

        while left < right:

            currSum = nums[preIndex] + nums[left] + nums[right]

            if currSum < target:
                totalSmallerTriplets += right - left
                left += 1
            elif currSum >= target:
                right -= 1
        return totalSmallerTriplets


if __name__ == "__main__":
    threeSumSmaller = ThreeSumSmaller()
    print(threeSumSmaller.numberOfTripletsSmallerToTarget([-2, 0, 1, 3, -3], 2))
    print(threeSumSmaller.numberOfTripletsSmallerToTarget([-2, 0, 1, 3], 2))
    print(threeSumSmaller.numberOfTripletsSmallerToTarget([], 0))
    print(threeSumSmaller.numberOfTripletsSmallerToTarget([0], 0))
