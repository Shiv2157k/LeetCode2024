from typing import List


class Intervals:

    def insert_intervals_v1(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Approach: Binary Search
        T: O(N)
        S: O(N)
        :param intervals:
        :param new_interval:
        :return:
        """

        if not intervals:
            return [new_interval]

        total_intervals = len(intervals)
        target = new_interval[0]
        left = 0
        right = total_intervals - 1

        while left <= right:
            pivot = left + (right - left) // 2
            if intervals[pivot][0] < target:
                left = pivot + 1
            else:
                right = pivot - 1

        intervals.insert(left, new_interval)
        
        output = []

        for interval in intervals:

            if not output and output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(interval[1], output[-1][1])
        return output

    def insert_intervals_v0(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Approach: Simulation by steps
        T: O(N)
        S: O(1)
        :param intervals:
        :param new_interval:
        :return:
        """

        if not intervals:
            return [new_interval]

        output = []
        total_intervals = len(intervals)
        ptr = 0
        # Step 1: add all the intervals before new interval start time
        while ptr < total_intervals and intervals[ptr][1] < new_interval[0]:
            output.append(intervals[ptr])
            ptr += 1

        # Step 2: Merge and add new interval
        while ptr < total_intervals and intervals[ptr][0] <= new_interval[1]:
            new_interval[0] = min(intervals[ptr][0], new_interval[0])
            new_interval[1] = max(intervals[ptr][1], new_interval[1])
            ptr += 1

        output.append(new_interval)

        # Step 3: Add intervals right to the new intervals
        while ptr < total_intervals:
            output.append(intervals[ptr])
            ptr += 1

        return output
