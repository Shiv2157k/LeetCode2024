from typing import List


class Intervals:

    def insertV1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach: Binary Search
        T: O(N)
        S: O(N)
        :param intervals:
        :param newInterval:
        :return:
        """

        if not intervals:
            return [newInterval]

        length = len(intervals)
        left = 0
        right = length - 1
        target = newInterval[0]

        while left <= right:

            pivot = left + (right - left) // 2

            if intervals[pivot][0] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        intervals.insert(left, newInterval)

        result = []

        for interval in intervals:

            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

    def insertV0(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach: Linear Search
        T: O(N)
        S: O(1)
        :param intervals:
        :param newInterval:
        :return:
        """
        # already sorted
        # intervals.sort(key=lambda x: x[0])
        if not intervals:
            return [newInterval]

        updatedIntervals = []
        pointer = 0

        # Step 1: Add everything before new interval
        while pointer < len(intervals) and intervals[pointer][1] < newInterval[0]:
            updatedIntervals.append(intervals[pointer])
            pointer += 1

        # Step 2: merge necessary and add new Interval
        while pointer < len(intervals) and intervals[pointer][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[pointer][0])
            newInterval[1] = max(newInterval[1], intervals[pointer][1])
            pointer += 1
        updatedIntervals.append(newInterval)

        # Step 3: add remaining intervals
        while pointer < len(intervals):
            updatedIntervals.append(intervals[pointer])
            pointer += 1

        return updatedIntervals
