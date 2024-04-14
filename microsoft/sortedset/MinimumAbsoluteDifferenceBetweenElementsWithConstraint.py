from typing import List
from sortedcontainers import SortedSet
from sys import maxsize


class MinimumAbsoluteDifferenceWithConstraints:

    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        Approach: Sorted Set
        T: O(N log N)
        S: O(N)
        :param nums:
        :param x:
        :return:
        """

        sortedSet = SortedSet()
        minAbsDiff = max(nums)

        for i in range(len(nums) - x - 1, -1, -1):

            sortedSet.add(nums[i + x])

            low = sortedSet.bisect_left(nums[i] + 1)
            high = sortedSet.bisect_right(nums[i])

            if low > 0:
                minAbsDiff = min(minAbsDiff, abs(sortedSet[low - 1] - nums[i]))
            if high < len(sortedSet):
                minAbsDiff = min(minAbsDiff, abs(sortedSet[high] - nums[i]))
        return minAbsDiff


if __name__ == "__main__":
    minAbsDiff = MinimumAbsoluteDifferenceWithConstraints()
    print(minAbsDiff.minAbsoluteDifference([4, 3, 2, 4], 1))

    print(minAbsDiff.minAbsoluteDifference([1, 2, 2, 3, 4], 2))
