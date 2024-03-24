from typing import List


class TimeIntervals:

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
        totalIntervals = len(intervals)
        target = newInterval[0]

        left, right = 0, totalIntervals - 1

        # [[1,2], [3,5], [6,7], [8,10], [12,16]]
        #               [4,8]
        while left <= right:
            pivot = left + (right - left) // 2

            if intervals[pivot][0] < target:
                left = pivot + 1
            else:
                right = pivot - 1

        intervals.insert(left, newInterval)

        updatedIntervals = []

        for interval in intervals:

            if not updatedIntervals or updatedIntervals[-1][1] < interval[0]:
                updatedIntervals.append(interval)
            else:
                updatedIntervals[-1][1] = max(updatedIntervals[-1][1], interval[1])
        return updatedIntervals

    def insertV0(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach: Linear
        T: O(N)
        S: O(N)
        :param intervals:
        :param newInterval:
        :return:
        [[1,2], [3,5], [6,7], [8,10], [12,16]]
        [4,8]
        """
        totalIntervals = len(intervals)
        updatedIntervals = []
        index = 0
        # Example: [[1,2], [3,5], [6,7], [8,10], [12,16]]
        # newInterval: [4,8]
        # Step 1: Add non-overlaps before merge
        # [1,2]
        while index < totalIntervals and intervals[index][1] < newInterval[0]:
            updatedIntervals.append(intervals[index])
            index += 1

        # Step 2: merge intervals if any
        while index < totalIntervals and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1
        updatedIntervals.append(newInterval)

        # Step 3: Add non overlaps after merge
        while index < totalIntervals:
            updatedIntervals.append(intervals[index])
            index += 1

        return updatedIntervals


if __name__ == "__main__":
    time_intervals = TimeIntervals()
    print(time_intervals.insertV0([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(time_intervals.insertV1([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))

    print(time_intervals.insertV0([[1, 3], [6, 9]], [2, 5]))
    print(time_intervals.insertV1([[1, 3], [6, 9]], [2, 5]))
