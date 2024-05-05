from typing import List
from math import inf


class NonOverlappingIntervals:

    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        """
        Approach: Sort
        T: O(N log N)
        S: O(1)
        :param intervals:
        :return:
        """

        # sort by end time as it gives more choices in minimizing
        # removal of interval nodes
        intervals.sort(key=lambda x: x[1])

        min_intervals: int = 0
        k: float = -inf

        for start, end in intervals:
            if start >= k:
                k = end
            else:
                min_intervals += 1
        return min_intervals
