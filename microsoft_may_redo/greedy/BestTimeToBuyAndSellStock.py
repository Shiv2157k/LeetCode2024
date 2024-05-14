from typing import List


class BestTimeToBuyAndSellStock:

    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        max_profit = 0
        min_price = prices[0]

        for day in range(1, len(prices)):

            if min_price > prices[day]:
                min_price = prices[day]
            if max_profit < prices[day] - min_price:
                max_profit = prices[day] - min_price
        return max_profit
