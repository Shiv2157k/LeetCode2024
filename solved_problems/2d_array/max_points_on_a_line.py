from typing import List


class Graph:

    def maxPointsOnALine(self, points: List[List[int]]) -> int:
        """
        Approach: Hash Map
        Time complexity: O(N ^ 2)
        Space Complexity: O(N)
        :param points:
        :return:
        """
        # minimum max point will be one
        maxPoints = 1
        totalPoints = len(points)
        # Loop over the total points and compare adjacent points
        for i in range(totalPoints):
            p1 = points[i]
            # to track the slope occurrence to understand points fall under this slope
            # Key: CalculatedSlope, Val: Occurrence
            # collections.Counter()
            slopeMap = dict()
            # start from i + 1 to ensure we do not overlap
            for j in range(i + 1, totalPoints):
                p2 = points[j]
                # to handle parallels we look at x-axis of two
                # points are on the same line and mark it as infinite
                if p1[0] == p2[0]:
                    slope = float("-inf")
                else:  # calculate slope by formula (y2 - y1)/(x2 - x1)
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                # our result will be max previous result vs the current slope occurence
                slopeMap[slope] = slopeMap.get(slope, 0) + 1
                # note: slopeMap[slope] + 1 -> because we did not included the current point
                maxPoints = max(maxPoints, slopeMap[slope] + 1)
        return maxPoints


if __name__ == "__main__":
    graph = Graph()
    print(graph.maxPointsOnALine([[1, 1], [2, 2], [3, 3]]))
    print(graph.maxPointsOnALine([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
