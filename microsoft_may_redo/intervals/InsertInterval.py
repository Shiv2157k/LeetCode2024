from typing import List


class Intervals:

    def insert_interval(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Approach: Pointer
        T: O(N)
        S: O(1)
        :param intervals:
        :param new_interval:
        :return:
        """

        total_intervals = len(intervals)
        output_intervals = []
        pointer = 0

        # Step 1: add all intervals before new interval start time
        while pointer < total_intervals and intervals[pointer][1] < new_interval[0]:
            output_intervals.append(intervals[pointer])
            pointer += 1

        # Step 2: merge any intervals and new interval
        while pointer < total_intervals and intervals[pointer][0] <= new_interval[0]:
            new_interval[0] = min(new_interval[0], intervals[pointer][0])
            new_interval[1] = max(new_interval[1], intervals[pointer][1])
            pointer += 1
        output_intervals.append(new_interval)

        # Step 3: Add the remaining
        while pointer < total_intervals:
            output_intervals.append(intervals[pointer])
            pointer += 1
        return output_intervals

