from typing import List


class LargestNumberKey(str):

    def __lt__(self: str, y: str):
        return self + y > y + self


class LargestNumber:

    def largestNumber(self, nums: List[int]) -> str:

        stringNumber = []
        for num in nums:
            stringNumber.append(str(num))

        stringNumber = sorted(stringNumber, key=LargestNumberKey)

        if stringNumber[0] == '0':
            return '0'
        else:
            ''.join(stringNumber)
