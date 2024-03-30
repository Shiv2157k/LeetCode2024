from typing import List


class ThreeSum:

    def allNonDuplicateCombinationsV1(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for index in range(len(nums)):
            if nums[index] > 0:
                break
            if index == 0 or nums[index] != nums[index - 1]:
                self._twoSumV1(nums, index, result)

        return result

    def _twoSumV1(self, nums: List[int], preIndex: int, result: List[int]) -> None:
        """
        :param nums:
        :param preIndex:
        :param result:
        :return:
        """
        left = preIndex + 1
        seen = set()

        while left < len(nums):

            complement = -nums[preIndex] - nums[left]
            if complement in seen:
                result.append([complement, nums[preIndex], nums[left]])
                while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                    left += 1
            seen.add(nums[left])
            left += 1

    def allNonDuplicateCombinationsV0(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointer
        T: O(N^2) -> O(N log N * N^2)
        S: O(log n) to O(N)
        :param nums:
        :return:
        """

        if not nums:
            return []

        result = []

        for index in range(len(nums)):

            # cannot meet target as next numbers are positive numbers
            if nums[index] > 0:
                break

            # current index is fixed and we go over all the next index combinations
            if index == 0 or nums[index] != nums[index - 1]:
                self._twoSum(nums, index, result)
        return result

    def _twoSum(self, nums: List[int], preIndex: int, result: List[int]) -> None:
        first = nums[preIndex]
        left = preIndex + 1
        right = len(nums) - 1

        while left < right:
            second = nums[left]
            third = nums[right]
            target = first + second + third

            if target == 0:
                result.append([first, second, third])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif target < 0:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    threeSum = ThreeSum()
    print(threeSum.allNonDuplicateCombinationsV0([-1, 0, 1, 2, -1, 4]))
    print(threeSum.allNonDuplicateCombinationsV0([0, 1, 1]))

    print(threeSum.allNonDuplicateCombinationsV1([-1, 0, 1, 2, -1, 4]))
    print(threeSum.allNonDuplicateCombinationsV1([0, 1, 1]))
