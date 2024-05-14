from typing import List
from collections import defaultdict


class MaximumNumberOfIntersectionsOnLine:

    def max_intersection_count(self, y: List[int]) -> int:
        """
        Approach: Tree Map (Sweep Line)
        T: O((n - 1) * log m) + O(M) | O(N log N) worst case
        S: O(N)
        :param y:
        :return:
        """

        n = len(y)
        sweep_line = {}
        max_intersections = 0
        curr_intersections = 0

        for i in range(1, n):
            start = 2 * y[i - 1]
            end = 2 * y[i] + (0 if i == n - 1 else (-1 if y[i] > y[i - 1] else 1))

            left = min(start, end)
            right = max(start, end) + 1

            sweep_line[left] = sweep_line.get(left, 0) + 1
            sweep_line[right] = sweep_line.get(right, 0) - 1

        sweep_line = dict(sorted(sweep_line.items()))

        for count in sweep_line.values():
            curr_intersections += count
            max_intersections = max(max_intersections, curr_intersections)
        return max_intersections
