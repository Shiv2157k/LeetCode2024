from typing import List


class Array:

    def find_all_duplicates_v3(self, nums: List[int]) -> List[int]:

        duplicates = []

        for num in nums:

            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            num[abs(num) - 1] *= -1
        return duplicates

    def find_all_duplicates_v2(self, nums: List[int]) -> List[int]:
        """
        Approach: Inplace ideal
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        duplicates: List[int] = []

        for num in nums:
            nums[abs(num) - 1] *= -1

        for num in nums:
            if nums[abs(num) - 1] > 0:
                duplicates.append(abs(num))
                nums[abs(num) - 1] *= -1
        return duplicates

    def find_all_duplicates_v1(self, nums: List[int]) -> List[int]:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        ptr = 0
        length = len(nums)
        duplicates = []

        while ptr < length:

            ideal_ptr = nums[ptr] - 1

            if nums[ideal_ptr] != nums[ptr]:
                nums[ideal_ptr], nums[ptr] = nums[ptr], nums[ideal_ptr]
            else:
                ptr += 1

        for i in range(length):
            if nums[i] != i + 1:
                duplicates.append(nums[i])
        return duplicates

    def find_all_duplicates_v0(self, nums: List[int]) -> List[int]:
        """
        Approach: hash set
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        duplicates = []
        seen = set()

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates
