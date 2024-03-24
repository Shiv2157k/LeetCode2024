from typing import List


class MeetingRooms:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Approach: Sort
        T: O(N log N)
        S: O(1)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])

        for index in range(1, len(intervals)):
            if intervals[index - 1][1] > intervals[index][0]:
                return False
        return True


if __name__ == "__main__":
    meetingRooms = MeetingRooms()
    print(meetingRooms.canAttendMeetings([[7, 10], [2, 4]]))
    print(meetingRooms.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
