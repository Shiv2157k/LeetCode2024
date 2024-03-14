import heapq
from typing import List


class MeetingRoomII:

    def minimum_rooms_required_v1(self, intervals: List[List[int]]) -> int:
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
        min_rooms = []
        heapq.heappush(min_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if min_rooms[0] <= interval[0]:
                heapq.heappop(min_rooms)
            heapq.heappush(min_rooms, interval[1])
        return len(min_rooms)

    def minimum_rooms_required(self, intervals: List[List[int]]) -> int:
        """
        Approach: Chronological Ordering
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """

        if not intervals:
            return 0

        sorted_start_time = sorted([interval[0] for interval in intervals])
        sorted_end_time = sorted([interval[1] for interval in intervals])
        start_pointer = end_pointer = 0
        total_intervals = len(intervals)
        used_rooms = 0
        while start_pointer < total_intervals:
            if sorted_start_time[start_pointer] >= sorted_end_time[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1
        return used_rooms


if __name__ == "__main__":
    meeting_room = MeetingRoomII()
    print(meeting_room.minimum_rooms_required_v1([(1, 3), (3, 5), (7, 8)]))
    print(meeting_room.minimum_rooms_required_v1([(1, 6), (3, 5), (7, 8)]))
    print(meeting_room.minimum_rooms_required([(1, 3), (3, 5), (7, 8)]))
    print(meeting_room.minimum_rooms_required([(1, 6), (3, 5), (7, 8)]))
