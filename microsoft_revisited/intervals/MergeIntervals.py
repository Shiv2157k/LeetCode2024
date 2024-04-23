from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]):
        """
        Approach:
        T: O(N log N)
        S: O(1)
        :param intervals:
        :return:
        """

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):

            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
