from typing import List


class PolygonWithLargestPerimeter:

    def findLargest(self, nums: List[int]) -> int:
        """
        Approach: Sorting and Greedy
        T: O(N log N)
        S: O(N)
        :param nums:
        :return:
        """

        nums.sort()
        sumSoFar = 0
        largestPerimeter = -1

        for num in nums:
            if num < sumSoFar:
                largestPerimeter = sumSoFar + num
            sumSoFar += num
        return largestPerimeter
