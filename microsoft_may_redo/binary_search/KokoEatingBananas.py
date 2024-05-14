from typing import List
from math import ceil


class KokoEatingBananas:

    def min_eating_speed(self, piles: List[int], h: int) -> int:
        """
        Approach: Binary Search
        t: O(N log M)
        S: O(1)
        :param piles:
        :param h:
        :return:
        """

        right = max(piles)
        left = ceil(sum(piles) / h)

        while left <= right:

            pivot = left + (right - left) // 2
            hour_spent = 0

            for pile in piles:
                hour_spent += ceil(pile / pivot)

            if hour_spent <= h:
                right = pivot
            else:
                left = pivot + 1
        return right
