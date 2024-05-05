from typing import List


class Chocolates:

    def buy_choco(self, prices: List[int], money: int) -> int:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param prices:
        :param money:
        :return:
        """

        if len(prices) < 2:
            return money

        first_min = min(prices[0], prices[1])
        second_min = max(prices[0], prices[1])

        for i in range(2, len(prices)):

            if prices[i] < first_min:
                second_min = first_min
                first_min = prices[i]
            elif prices[i] < second_min:
                second_min = prices[i]

        min_cost = first_min + second_min

        if min_cost <= money:
            return money - min_cost
        else:
            return money
