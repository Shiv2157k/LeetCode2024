from typing import List


class BestTimeToBuyAndSellStock:

    def max_profit_made_v1(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        max_profit = 0

        for day in range(1, len(prices)):
            if prices[day] > prices[day - 1]:
                max_profit += prices[day] - prices[day - 1]
        return max_profit

    def max_profit_made_v0(self, prices: List[int]) -> int:
        """
        Approach: Peak and Valley
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        ptr = 0
        max_profit = 0

        while ptr < len(prices) - 1:

            while ptr < len(prices) - 1 and prices[ptr] >= prices[ptr + 1]:
                ptr += 1
            valley = prices[ptr]

            while ptr < len(prices) - 1 and prices[ptr] <= prices[ptr + 1]:
                ptr += 1
            peak = prices[ptr]

            max_profit += peak - valley
        return max_profit
