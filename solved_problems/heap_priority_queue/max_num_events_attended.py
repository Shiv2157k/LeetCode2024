from heapq import heappop, heappush
from typing import List


class Events:

    def __get_total_days(self, events: List[List[int]]):
        total_days = 0
        for start_date in range(len(events)):
            total_days = max(total_days, events[start_date][1])
        return total_days

    def max_events_attended(self, events: List[List[int]]):
        """
        Approach: Heapq
        T: O(N log N)
        S: O(N)
        :param events:
        :return:
        """
        events = sorted(events, key=lambda e: (e[0], e[1]))
        total_days = self.__get_total_days(events)

        start_event_day = 0
        events_attended = 0
        end_days = []

        for curr_day in range(1, total_days + 1):

            # step 1: add same day events end date into heapq
            while start_event_day < len(events) and events[start_event_day][0] == curr_day:
                heappush(end_days, events[start_event_day][1])
                start_event_day += 1

            # step 2: pop out expired events on the current day
            while end_days and end_days[0] < curr_day:
                heappop(end_days)

            # step 3: add the events of the current day note: 1 event / day
            if end_days:
                heappop(end_days)
                events_attended += 1
        return events_attended


if __name__ == "__main__":
    events = Events()
    print(events.max_events_attended(
        [
            [1, 2], [1, 3], [1, 2], [3, 4], [4, 4], [4, 5]
        ]
    ))
    print(events.max_events_attended(
        [
            [1, 2], [1, 2]
        ]
    ))
    print(events.max_events_attended(
        [
            [1, 2], [1, 1]
        ]
    ))
    print(events.max_events_attended(
        [
            [1, 1]
        ]
    ))





