from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Interval:

    def __init__(self, start: float, end: float, close_start: bool, close_end: bool):
        self.start = start
        self.end = end
        self.close_start = close_start
        self.close_end = close_end

    def __lt__(self, other):
        return self.end < other.end or (self.end == other.end and other.close_end)


class MaxNoOfIntersectionOnChart:

    def max_intersection_count_v1(self, y: List[int]):
        """
        Approach: TreeMap
        T: O((n-1)*log m) + O(m) | O(n log n) worst case
        S: O(n)
        :param y:
        :return:
        """
        n = len(y)  # Number of elements in the array y
        max_intersections = 0  # Holds the maximum intersection count
        current_intersection_count = 0  # Tracks the current count of intersections
        sweep_line = defaultdict(int)  # Dictionary to simulate the sweep line algorithm

        # Iterate over the elements of the array to populate the Dictionary
        for i in range(1, n):
            # Calculate the starting point of the line segment
            # (to handle the situation where the start and end y-values could be half values,
            # since points can intersect at mid-points between integer y-values)
            start = 2 * y[i - 1]
            # Calculate the ending point of the line segment
            # Adjust for the last point or if the current y is more than the previous y
            end = 2 * y[i] + (0 if i == n - 1 else (-1 if y[i] > y[i - 1] else 1))
            # Merge the start points into Dictionary, incrementing the count for intersections
            sweep_line[min(start, end)] += 1
            # Merge the end points into Dictionary, decrementing the count for intersections
            sweep_line[max(start, end) + 1] -= 1

        # Sort the Dictionary by keys
        sweep_line = dict(sorted(sweep_line.items()))

        # Iterate through the Dictionary
        for count in sweep_line.values():
            # Update the current intersection count
            current_intersection_count += count
            # Update the maximum intersection count found so far
            max_intersections = max(max_intersections, current_intersection_count)

        return max_intersections

    def max_intersection_count_v0(self, y: List[int]) -> int:

        intervals = []

        intervals.append(Interval(y[0], y[0], True, True))

        for i in range(1, len(y)):

            if y[i - 1] < y[i]:
                intervals.append(Interval(y[i - 1], y[i], False, True))
            else:
                intervals.append(Interval(y[i], y[i - 1], True, False))

        intervals.sort(key=lambda x: (x.start, not x.close_start))

        intersections = []  # min heap
        max_size = 0

        for interval in intervals:

            while intersections and (intersections[0].end < interval.start or (
                    intersections[0].end == interval.start and not intersections[0].close_end) or (
                                             intersections[0].end == interval.start and not interval.close_start)):
                heappop(intersections)

            heappush(intersections, interval)
            max_size = max(max_size, len(intersections))
        return max_size
