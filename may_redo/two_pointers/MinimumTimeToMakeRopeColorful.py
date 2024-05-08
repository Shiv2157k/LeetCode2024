from typing import List


class MakeRopeColorful:

    def minimum_time_needed_v1(self, colors: str, needed_time: List[int]) -> int:
        """
        Approach: Two Pointers Advanced
        T: O(N)
        S: O(1)
        :param colors:
        :param needed_time:
        :return:
        """

        total_time = 0
        curr_max_time = 0
        for i in range(len(colors)):

            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0

            total_time += min(curr_max_time, needed_time[i])
            curr_max_time = max(curr_max_time, needed_time[i])
        return total_time

    def minimum_time_needed_v0(self, colors: str, needed_time: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param colors:
        :param needed_time:
        :return:
        """

        total_time = 0
        left = 0
        right = 0

        while left < len(needed_time) and right < len(needed_time):

            curr_sum = 0
            curr_max_time = 0

            while right < len(needed_time) and colors[left] == colors[right]:
                curr_sum += needed_time[right]
                curr_max_time = max(curr_max_time, needed_time[right])

            total_time += curr_sum - curr_max_time
        return total_time
