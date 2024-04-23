from typing import List
from math import ceil


class KokoEatingBananas:

    def minEatingSpeedV0(self, piles: List[int], h: int) -> int:
        """
        Approach: Brute Force
        T: O(M * N)
        S: O(1)
        :param piles:
        :param h:
        :return:
        """
        speed = 1

        while True:

            hourSpent = 0

            for pile in piles:
                hourSpent += ceil(pile / h)

            if hourSpent <= h:
                return speed
            else:
                speed += 1

    def minEatingSpeedV1(self, piles: List[int], h: int) -> int:
        """
        Approach: Binary Search
        T: O(N log M)
        S: O(1)
        :param piles:
        :param h:
        :return:
        """

        # on an average min bananas koko can eat is sum(piles) / h
        left = ceil(sum(piles) / h)
        right = max(piles)

        while left < right:

            pivot = left + (right - left) // 2
            hourSpent = 0

            for pile in piles:
                hourSpent += ceil(pile / h)

            if hourSpent <= h:
                right = pivot
            else:
                left = pivot + 1
        return right