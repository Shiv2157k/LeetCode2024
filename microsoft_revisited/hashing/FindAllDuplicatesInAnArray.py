from typing import List, Set


class DuplicateArray:

    def find_duplicatesV3(self, nums: List[int]) -> List[int]:
        """
        Approach: Hash
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        duplicates: List[int] = []

        for num in nums:

            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            nums[abs(num) - 1] *= -1
        return duplicates


    def find_duplicatesV2(self, nums: List[int]) -> List[int]:
        """
        Approach: Hash
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

    def find_duplicatesV1(self, nums: List[int]) -> List[int]:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        ptr: int = 0
        n: int = len(nums)

        while ptr < n:
            insert_ptr = nums[ptr] - 1

            if nums[ptr] != nums[insert_ptr]:
                nums[ptr], nums[insert_ptr] = nums[insert_ptr], nums[ptr]
            else:
                ptr += 1

        duplicates: List[int] = []

        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])
        return duplicates


    def find_duplicatesV0(self, nums: List[int]) -> List[int]:
        """
        Approach: Hash Set
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        seen: Set[int] = set()
        result: List[int] = []

        for num in nums:

            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return result