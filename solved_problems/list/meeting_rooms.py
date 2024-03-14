from typing import List


class MeetingRoom:

    def total_non_overlapping_rooms_v1(self, intervals: List[List[int]]) -> bool:
        """
        Approach: Sorting
        T: O(N log N)
        S: O(N)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        for index in range(1, len(intervals)):
            if intervals[index - 1][1] > intervals[index][0]:
                return False
        return True

    def total_non_overlapping_rooms(self, intervals: List[List[int]]) -> bool:
        """
        Approach: Brute Force
        T: O(N^2)
        S: O(N)
        :param intervals:
        :return:
        """

        def overlap(interval1, interval2):
            return (
                    interval1[0] >= interval2[0] and interval1[0] < interval2[1] or
                    interval2[0] >= interval1[0] and interval2[0] < interval1[1]
            )

        n = len(intervals)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True


if __name__ == "__main__":
    meeting_room = MeetingRoom()
    print(meeting_room.total_non_overlapping_rooms([(1, 3), (3, 5), (7, 8)]))
    print(meeting_room.total_non_overlapping_rooms([(1, 6), (3, 5), (7, 8)]))
    print(meeting_room.total_non_overlapping_rooms_v1([(1, 3), (3, 5), (7, 8)]))
    print(meeting_room.total_non_overlapping_rooms_v1([(1, 6), (3, 5), (7, 8)]))
