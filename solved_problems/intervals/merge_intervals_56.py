from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Sort
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged


if __name__ == "__main__":
    merge_intervals = Intervals()
    print(merge_intervals.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals.merge([[1, 4], [4, 5]]))
