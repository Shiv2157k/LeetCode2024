from typing import List
from math import inf


class MaxPoints:

    def on_a_line(self, points: List[List[int]]) -> int:
        """
        Approach: Math
        Formula: y2 - y1 / x2 - x1
        T: O(N)
        S: O(N)
        :param points:
        :return:
        """

        max_points: int = 1
        total_points = len(points)

        for i in range(total_points):
            p1 = points[i]
            slope_map = {}

            for j in range(i + 1, total_points):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = -inf  # to handle straight or parallel line
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                slope_map[slope] = slope_map.get(slope, 0) + 1
                max_points = max(max_points, slope_map[slope] + 1)
        return max_points
