from typing import List


class ColorfulRope:

    def minimum_time_v1(self, colors: str, needed_time: List[int]) -> int:
        """
        Approach: One Pass Advanced
        T: O(N)
        S: O(1)
        :param colors:
        :param needed_time:
        :return:
        """

        total_time = 0
        curr_max = 0

        for i in range(len(colors)):

            if i > 0 and colors[i - 1] != colors[i]:
                curr_max = 0
            total_time += min(needed_time[i], curr_max)
            curr_max = max(curr_max, needed_time)
        return total_time


    def minimum_time(self, colors: str, needed_time: List[int]) -> int:
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
            curr_max = 0

            while right < len(needed_time) and colors[left] == colors[right]:
                curr_sum += needed_time[right]
                curr_max = max(curr_max, needed_time[right])
                right += 1

            total_time += curr_sum - curr_max
            left = right
        return total_time