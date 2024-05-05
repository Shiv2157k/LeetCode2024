from typing import List


class Temperatures:

    def daily(self, temperatures: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param temperatures:
        :return:
        """

        stack = []
        output = [0] * len(temperatures)

        for curr_day, temperature in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                output[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return output
