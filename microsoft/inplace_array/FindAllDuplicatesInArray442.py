from typing import List


class FindAllDuplicates:

    def findV3(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Negation
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        result = []

        for num in nums:
            if nums[abs(num - 1)] < 0:
                result.append(abs(num))
            nums[abs(num - 1)] *= -1
        return result

    def findV2(self, nums: List[int]) -> List[int]:
        """
        Approach: Negation
        T: O(N)
        S: O(N) -> auxilary space
        :param nums:
        :return:
        """
        result = []
        for num in nums:
            nums[abs(num) - 1] *= -1

        for num in nums:
            if nums[abs(num) - 1] > 0:
                result.append(abs(num))
                nums[abs(num) - 1] *= -1
        return result

    def findV1(self, nums: List[int]) -> List[int]:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        index = 0
        result = []

        while index < len(nums):
            insertIndex = nums[index] - 1
            if nums[index] != nums[insertIndex]:
                # swap
                nums[index], nums[insertIndex] = nums[insertIndex], nums[index]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result

    def findV0(self, nums: List[int]) -> List[int]:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        seen = set()
        result = []

        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return result
