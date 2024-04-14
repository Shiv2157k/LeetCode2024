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

        # sort based on start time
        intervals.sort(key=lambda x: x[0])

        mergedIntervals = [intervals[0]]

        for index in range(1, len(intervals)):
            if mergedIntervals[-1][-1] >= intervals[index][0]:
                if mergedIntervals[-1][1] < intervals[index][1]:
                    mergedIntervals[-1][1] = intervals[index][1]
            else:
                mergedIntervals.append(intervals[index])
        return mergedIntervals


if __name__ == "__main__":
    i = Intervals()
    print(i.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
