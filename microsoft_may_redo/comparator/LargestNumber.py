from typing import List


class LargestNumberKey(str):

    def __lt__(self: str, y: str):
        return self + y > y + self


class LargestNumber:

    def get_largest_number(self, nums: List[int]) -> str:
        """
        Approach: Comparator Sort
        T: O(N log N)
        S: O(N)
        :param nums:
        :return:
        """

        string_number = []
        for num in nums:
            string_number.append(str(num))

        string_number = sorted(string_number, key=LargestNumberKey)

        if string_number[0] == '0':
            return '0'
        return ''.join(string_number)

    def get_largest_number_v0(self, nums: List[int]) -> str:
        """
        Approach: Bubble Sort
        T: O(N^2) - worst  case
        S: O(1)
        :param nums:
        :return:
        """

        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if self._compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if nums[0] == 0:
            return '0'
        result = []
        for num in nums:
            result.append(str(num))
        return ''.join(result)

    def _compare(self, n1: int, n2: int):
        return str(n1) + str(n2) > str(n2) + str(n1)
