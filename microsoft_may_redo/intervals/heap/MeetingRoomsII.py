from typing import List
from heapq import heappop, heappush


class MeetingRoomsII:

    def min_rooms_required(self, intervals: List[List[int]]) -> int:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        intervals.sort(key=lambda x: x[0])

        min_rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):

            if min_rooms[0] <= intervals[i][0]:
                heappop(min_rooms)
            heappush(min_rooms, intervals[i][1])
        return len(min_rooms)
