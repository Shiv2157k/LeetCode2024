from typing import List


class FourSum:

    def generateFourSumCombinationsV1(self, nums: List[int], target: int):
        """
        Approach: Two Pointers Recursion
        :param nums:
        :param target:
        :return:
        """

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []
            # base cases
            if not nums:
                return result

            averageVal = target // k

            if averageVal < nums[0] or nums[-1] < averageVal:
                return result

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        result.append([nums[i]] + subset)
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            left, right = 0, len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif currSum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return result

        nums.sort()
        return kSum(nums, target, 4)

    def generateFourSumCombinationsV0(self, nums: List[int], target: int):
        """
        Approach: Two Pointers
        T: O(N ^ 3)
        S: O(N)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        result = []
        length = len(nums)

        for p1 in range(length - 3):

            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            if nums[p1] * 4 > target:
                break

            for p2 in range(p1 + 1, length - 2):

                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                if nums[p2] * 3 > target - nums[p1]:
                    break

                p3, p4 = p2 + 1, length - 1

                while p3 < p4:

                    currentSum = nums[p1] + nums[p2] + nums[p3] + nums[p4]

                    if currentSum == target:
                        result.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        while p3 < p4 and nums[p3] == nums[p3 + 1]:
                            p3 += 1
                        while p3 < p4 and nums[p4] == nums[p4 - 1]:
                            p4 -= 1
                        p3 += 1
                        p4 -= 1
                    elif currentSum < target:
                        p3 += 1
                    else:
                        p4 -= 1
        return result


if __name__ == "__main__":
    fourSum = FourSum()
    print(fourSum.generateFourSumCombinationsV0([1, 0, -1, 0, -2, 2], 0))
    print(fourSum.generateFourSumCombinationsV1([1, 0, -1, 0, -2, 2], 0))

    print(fourSum.generateFourSumCombinationsV0([2, 2, 2, 2], 8))
    print(fourSum.generateFourSumCombinationsV1([2, 2, 2, 2], 8))
