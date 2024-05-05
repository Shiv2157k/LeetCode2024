from typing import List
from math import inf


class BestTimeToBuyAndSellStocksIII:

    def max_profit_v1(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        t1_price = inf
        t2_price = inf
        t1_profit = 0
        t2_profit = 0

        for price in prices:
            t1_price = min(t1_price, price)
            t1_profit = max(t1_profit, price - t1_price)

            t2_price = min(t2_price, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_price)
        return t2_profit

    def max_profit_v0(self, prices: List[int]) -> int:
        """
        Approach: two arrays
        T: O(N)
        S: O(N)
        :param prices:
        :return:
        """

        total_days = len(prices)
        if total_days <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        left_profits = [0] * total_days
        right_profits = [0] * (total_days + 1)

        for left in range(1, total_days):
            left_profits[left] = max(left_profits[left], prices[left] - left_min)
            left_min = min(left_min, prices[left])

            right = total_days - 1 - left
            right_profits[right] = max(right_profits[right + 1], right_max - prices[right])
            right_max = max(right_max, prices[right])

        max_profit = 0

        for i in range(total_days):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
        return max_profit
