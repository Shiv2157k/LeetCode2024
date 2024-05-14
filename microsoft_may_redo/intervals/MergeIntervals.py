from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T: O(N log N) -> As we are sorting
        S: O(1) not considering output
        """

        #  sort the intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):

            if merged_intervals[-1][1] >= intervals[i][0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals