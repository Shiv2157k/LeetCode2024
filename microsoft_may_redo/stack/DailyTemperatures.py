from typing import List


class DailyTemperatures:

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param temperatures:
        :return:
        """

        output = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                output[prev_day] = day - prev_day
            stack.append(day)
        return output
