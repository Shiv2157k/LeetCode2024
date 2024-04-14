from typing import List


class Line:

    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Approach: Math Slope = (y2 - y1) / (x2 - x1)
        T: O(N)
        S: O(N)
        :param points:
        :return:
        """

        maxPoints = 1
        totalPoints = len(points)

        for i in range(totalPoints):

            p1 = points[i]
            slopeMap = {}
            for j in range(i + 1, totalPoints):

                p2 = points[j]

                # x is parallel to handle this case we mark it as infinite
                if p1[0] == p2[0]:
                    slope = float("-inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                slopeMap[slope] = slopeMap.get(slope, 0) + 1

                maxPoints = max(maxPoints, slopeMap[slope] + 1)
        return maxPoints


if __name__ == "__main__":
    line = Line()
    print(line.maxPoints([[1, 1], [2, 2], [3, 3]]))
