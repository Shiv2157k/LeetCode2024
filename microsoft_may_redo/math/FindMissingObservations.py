from typing import List


class FindMissingObservations:


    def missing_rolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Approach: Math
        T: O(N)
        S: O(1)
        :param rolls:
        :param mean:
        :param n:
        :return:
        """

        total_rolls = len(rolls)
        sum_rolled = 0
        for roll_val in rolls:
            sum_rolled += roll_val

        # this will give expected sum of the total
        total_expected_sum = mean * (n + total_rolls) - sum_rolled

        # - total expected sum cannot be less than n as we won't be able to divide to n values
        # - total expected sum is more than the max i.e., n * 6 we cannot form n values
        if total_expected_sum < n or total_expected_sum > n * 6:
            return []

        result = []

        while total_expected_sum != 0:
            # max for one dice will be 6 or less than than
            dice = min(total_expected_sum - n + 1, 6)
            result.append(dice)
            # decrement observations
            total_rolls -= dice
            # decrement n as we found one observation
            n -= 1
        return result