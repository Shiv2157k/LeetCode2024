from typing import List


class FourSum:

    def fourSumV1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Two Pointers
        T: O(N^k - 1) or O(N^3)
        S: O(N)
        :param nums:
        :param target:
        :return:
        """
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []

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
            output = []
            left = 0
            right = len(nums) - 1

            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == target:
                    output.append([nums[left], nums[right]])
                elif currSum < target:
                    left += 1
                else:
                    right -= 1
            return output
        nums.sort()
        return kSum(nums, target, 4)

    def fourSumV0(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        if not nums or len(nums) < 4:
            return result

        nums.sort()

        for firstIndex in range(len(nums) - 3):

            # checks
            if firstIndex > 0 and nums[firstIndex] == nums[firstIndex - 1]:
                continue

            if nums[firstIndex] * 4 > target:
                break

            for secondIndex in range(firstIndex, len(nums) - 2):

                if secondIndex > firstIndex + 1 and nums[secondIndex] == nums[secondIndex - 1]:
                    continue

                if nums[secondIndex] * 3 > target - nums[firstIndex]:
                    break

                left = secondIndex + 1
                right = len(nums) - 1

                while left < right:

                    currSum = nums[firstIndex] + nums[secondIndex] + nums[left] + nums[right]

                    if currSum == target:
                        result.append([nums[firstIndex], nums[secondIndex], nums[left],  nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif currSum < target:
                        left += 1
                    else:
                        right -= 1
        return result
