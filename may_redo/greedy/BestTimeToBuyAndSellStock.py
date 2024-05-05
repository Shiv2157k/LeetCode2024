from typing import List


class BestTimeToBuyAndSellStocks:

    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        min_price = prices[0]
        max_gain = 0

        for day in range(1, len(prices)):
            if prices[day] < min_price:
                min_price = prices[day]
            if max_gain < prices[day] - min_price:
                max_gain = prices[day] - min_price
        return max_gain
