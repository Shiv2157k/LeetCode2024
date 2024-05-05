from typing import List


class Dice:

    def missing_observations(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Approach: Math
        T: O(K) K -> totalExpectedSum
        S: O(n)
        :param rolls:
        :param mean:
        :param n:
        :return:
        """

        total_rolled: int = len(rolls)
        sum_of_rolled: int = 0

        for roll in rolls:
            sum_of_rolled += roll

        # calculation to figure out missing observations
        totalExpected = (mean * (n + total_rolled)) - sum_of_rolled

        # validation
        if totalExpected < n or totalExpected > n * 6:
            return []

        result = []

        while totalExpected != 0:
            # to make sure and keep balance b/w totalExpectedSum and n
            dice_rolled: int = min(totalExpected - n + 1, 6)
            result.append(dice_rolled)
            totalExpected -= dice_rolled
            n -= 1
        return result
