from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Sort and Merge
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):

            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output
