from typing import List
from math import inf

class NonOverlappingIntervals:


    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        """
        Approach: Sort
        T: O(N log N)
        S: O(N) -> worst case Timsort sorting
        :param intervals:
        :return:
        """

        # sort by end time as it gives more choices in minimizing removal
        intervals.sort(key=lambda x: x[1])

        k = -inf
        min_intervals = 0

        for start, end in intervals:

            if start >= k:
                k = end
            else:
                min_intervals += 1
        return min_intervals