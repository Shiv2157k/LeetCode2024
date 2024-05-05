import math
from typing import List
from math import ceil


class KokoEatingBananas:

    def min_eating_speed(self, piles: List[int], hour: int) -> int:
        """
        Approach: Binary Search
        T: O(N)
        S: O(1)
        :param piles:
        :return:
        """

        # maximum possibility koko can eat bananas
        max_bananas: int = 0
        total_bananas: int = 0

        for pile in piles:
            if max_bananas < pile:
                max_bananas = pile
            total_bananas += pile

        # on an average koko can eat minimum bananas per hour
        min_bananas = ceil(total_bananas / hour)

        while min_bananas < max_bananas:
            bananas = min_bananas + (max_bananas - min_bananas) // 2
            hour_spent: int = 0

            for pile in piles:
                hour_spent += math.ceil(pile / bananas)

            if hour_spent <= hour:
                max_bananas = bananas
            else:
                min_bananas = bananas + 1
        # max bananas she can eat
        return max_bananas


