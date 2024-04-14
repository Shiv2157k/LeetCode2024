from typing import List


class InsertIntervals:

    def insertV1(self, intervals: List[List[int]], newInterval: List[int]) -> List[int]:
        """
        Approach: Binary + Linear
        T: O(log N + N) -> O(N)
        S: O(N)
        :param intervals:
        :param newInterval:
        :return:
        """

        if not intervals:
            return [newInterval]

        length = len(intervals)
        left, right = 0, length - 1
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

    def insertV0(self, intervals: List[List[int]], newInterval: List[int]) -> List[int]:
        """
        Approach: Linear
        T: O(N)
        S: O(N)
        :param intervals:
        :return:
        """

        totalIntervals = len(intervals)
        newFormedIntervals = []

        index = 0

        # add non overlapping intervals before new intervals
        while index < totalIntervals and intervals[index][1] < newInterval[0]:
            newFormedIntervals.append(intervals[index])
            index += 1

        # merge intervals if any
        while index < totalIntervals and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1
        newFormedIntervals.append(newInterval)

        # add non overlapping after merge
        while index < totalIntervals:
            newFormedIntervals.append(intervals[index])
            index += 1
        return newFormedIntervals


if __name__ == "__main__":
    insertIntervals = InsertIntervals()
    print(insertIntervals.insertV0(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ))
    print(insertIntervals.insertV1(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ))

    print(insertIntervals.insertV0(
        [[1, 3], [6, 9]], [2, 5]
    ))
    print(insertIntervals.insertV1(
        [[1, 3], [6, 9]], [2, 5]
    ))
