from typing import List
from heapq import heappop, heappush


class MeetingRoomsII:

    def minMeetingRoomsV1(self, intervals: List[List[int]]) -> int:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        freeRooms = []
        heappush(freeRooms, intervals[0][1])

        for startTime, endTime in intervals[1:]:

            if freeRooms[0] <= startTime:
                heappop(freeRooms)
            heappush(freeRooms, endTime)
        return len(freeRooms)

    def minMeetingRoomsV2(self, intervals: List[List[int]]) -> int:
        """
        Approach: Chronological Ordering
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        if not intervals:
            return 0

        usedRooms = 0

        startTimes = sorted(interval[0] for interval in intervals)
        endTimes = sorted(interval[1] for interval in intervals)
        length = len(intervals)

        left, right = 0, 0

        while left < length:

            if startTimes[left] >= endTimes[right]:
                usedRooms -= 1
                right += 1
            usedRooms += 1
            left += 1
        return usedRooms

