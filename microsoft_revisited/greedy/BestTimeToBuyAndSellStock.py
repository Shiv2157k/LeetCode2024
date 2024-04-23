from typing import List


class BestTimeToBuyAndSellStock:

    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        minPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            if minPrice > prices[i]:
                minPrice = prices[i]
            if profit < prices[i] - minPrice:
                profit = profit[i] - minPrice
        return profit
