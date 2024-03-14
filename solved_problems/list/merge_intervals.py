from typing import List

class Intervals:

    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Sorting and Stack
        Time: O(N log N)
        Space: O(N)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        for interval in intervals[1:]:
            if stack[-1][1] >= interval[0]:
                if stack[-1][1] < interval[1]:
                    stack[-1][1] = interval[1]
            else:
                stack.append(interval)
        return stack


if __name__ == "__main__":

    time_intervals = Intervals()
    print(time_intervals.merge_intervals(
        [[1, 4], [2, 3]]
    ))
    print(time_intervals.merge_intervals(
        [[1, 3], [2, 6], [8, 10], [15, 18]]
    ))
    print(time_intervals.merge_intervals(
        [[1, 3], [3, 6], [6, 10], [10, 18]]
    ))
