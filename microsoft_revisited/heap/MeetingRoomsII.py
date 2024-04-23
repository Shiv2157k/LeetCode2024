from heapq import heappop, heappush
from typing import List


class MeetingRoomsII:

    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        """
        Approach: Min Heap
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        # sort the intervals by start time
        intervals.sort(key=lambda x: x[0])
        # this will act as our min heap
        meetings: List[int] = []
        heappush(meetings, intervals[0][1])

        for meeting in range(1, len(intervals)):

            if meetings[0] <= intervals[meeting][0]:
                heappop(meetings)
            heappush(meetings, intervals[meeting][1])

        return len(meetings)
