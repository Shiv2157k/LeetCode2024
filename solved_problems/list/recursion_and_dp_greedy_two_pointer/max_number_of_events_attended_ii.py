from typing import List


class Events:

    def search_next_pos(self, events: List[List[int]], curr_pos: int, last_pos: int) -> int:
        """
        Binary Search
        :param events:
        :param curr_pos:
        :param last_post:
        :return:
        """
        curr_end_day = events[curr_pos][1]
        curr_pos += 1
        while curr_pos < last_pos:
            pivot = curr_pos + (last_pos - curr_pos) // 2
            if events[pivot][0] > curr_end_day:
                last_pos = pivot
            else:
                curr_pos = pivot + 1
        return last_pos


    def max_number(self, events: List[List[int]], k: int) -> int:
        """
        Approach: Bottom Up DP
        :param events:
        :param k:
        :return:
        """
        # sort the events
        if k == 1:
            max_value = 0
            for event in events:
                max_value = max(max_value, event[2])
            return max_value

        events = sorted(events, key=lambda e: (e[0], e[1]))
        dp = [[-1] * (k + 1) for _ in range(len(events))]
        return self.depth_first_search(dp, events, 0, k, len(events))

    def max_number_(self, events: List[List[int]], k: int) -> int:
        """
        Approach: Top Down DP
        :param events:
        :param k:
        :return:
        """
        # sort the events
        if k == 1:
            max_value = 0
            for event in events:
                max_value = max(max_value, event[2])
            return max_value

        events = sorted(events, key=lambda e: (e[0], e[1]))
        dp = [[0] * (len(events) + 1) for _ in range(k + 1)]
        for curr_index in range(len(events) - 1, -1, -1):
            for count in range(1, k + 1):
                next_index = self.search_next_pos(events, curr_index, len(events))
                dp[count][curr_index] = max(dp[count][curr_index + 1], events[curr_index][2] + dp[count - 1][next_index])
        return dp[k][0]

    def depth_first_search(self, dp: List[List[int]], events: List[List[int]], position: int, k: int, total_events: int) -> int:

        # base case
        if position >= total_events or k == 0:
            return 0

        if dp[position][k] > -1:
            return dp[position][k]

        next_pos = self.search_next_pos(events, position, total_events)
        select = events[position][2] + self.depth_first_search(dp, events, next_pos, k - 1, total_events)
        reject = self.depth_first_search(dp, events, position + 1, k, total_events)
        dp[position][k] = max(select, reject)
        return dp[position][k]
