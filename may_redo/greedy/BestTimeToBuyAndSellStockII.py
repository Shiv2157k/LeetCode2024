from typing import List


class BestTimeToBuyAndSellStockII:

    def max_profit_v1(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        max_gain = 0

        for day in range(len(prices) - 1):

            if prices[day] < prices[day + 1]:
                max_gain += prices[day + 1] - prices[day]
        return max_gain

    def max_profit_v0(self, prices: List[int]) -> int:
        """
        Approach: Peak Valley
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        ptr = 0
        max_profit = 0

        while ptr < len(prices):

            while ptr < len(prices) - 1 and prices[ptr] >= prices[ptr + 1]:
                ptr += 1
            valley = prices[ptr]

            while ptr < len(prices) - 1 and prices[ptr] <= prices[ptr + 1]:
                ptr += 1
            peak = prices[ptr]

            max_profit += peak - valley
        return max_profit
