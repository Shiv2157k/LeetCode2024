from typing import List


class OverlappingIntervals:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Approach: Greedy
        T: O(N log N)
        S: O(N) / O(log N) -> Java uses Quicksort algorithm
        :param intervals:
        :return:
        """
        # we need to sort by end time as it gives us more choices
        # in minimizing the removal of interval nodes
        intervals.sort(key=lambda x: x[1])

        k = float("-inf")
        minIntervals = 0

        for start, end in intervals:
            # case 1: we can safely consider this interval because it won't cause overlap
            # update the k range to its end
            if start >= k:
                k = end
            # case 2: start < k will cause an overlap. We need to take intervals with earlier
            # end times. start > k, we must delete current interval and not update k
            else:
                minIntervals += 1
        return minIntervals


if __name__ == "__main__":
    overlappingIntervals = OverlappingIntervals()
    print(overlappingIntervals.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(overlappingIntervals.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(overlappingIntervals.eraseOverlapIntervals([[1, 2], [2, 3]]))
