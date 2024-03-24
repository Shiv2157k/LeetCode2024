from heapq import heappop, heappush
from typing import List


class MeetingRoomsII:

    def minMeetingRoomsV0(self, intervals: List[List[int]]) -> int:
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
        totalIntervals = len(intervals)

        left = right = 0

        while left < totalIntervals:

            if startTimes[left] >= endTimes[right]:
                usedRooms -= 1
                right += 1
            usedRooms += 1
            left += 1
        return usedRooms

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


if __name__ == "__main__":
    meetingRoomsII = MeetingRoomsII()
    print(meetingRoomsII.minMeetingRoomsV1([[0, 30], [5, 10], [15, 20]]))
    print(meetingRoomsII.minMeetingRoomsV1([[7, 10], [2, 4]]))
    print(meetingRoomsII.minMeetingRoomsV0([[0, 30], [5, 10], [15, 20]]))
    print(meetingRoomsII.minMeetingRoomsV0([[7, 10], [2, 4]]))
