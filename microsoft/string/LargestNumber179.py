from typing import List


class LargestNumberKey(str):

    def __lt__(x: str, y: str):
        return x + y > y + x


class LargestNumber:

    def getLargest(self, nums: List[int]) -> str:
        """
        Approach: Comparator
        T: O(N log N)
        S: O(N)
        :param nums:
        :return:
        """
        largestNumber = ''.join(sorted(map(str, nums), key=LargestNumberKey))
        return '0' if largestNumber[0] == '0' else largestNumber


if __name__ == "__main__":
    largest = LargestNumber()
    print(largest.getLargest([3, 30, 34, 5, 9]))