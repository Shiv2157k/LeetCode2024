from typing import List



class BuyStockII:

    def maxProfitV1(self, prices: List[List[int]]) -> int:
        """
        Approach: Single Pass
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        maxProfit = 0
        for day in range(len(prices) - 1):

            if prices[day] < prices[day + 1]:
                maxProfit += (prices[day + 1] - prices[day])
        return maxProfit

    def maxProfitV0(self, prices: List[List[int]]) -> int:
        """
        Approach: Peak Valley Approach
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        day = 0
        totalDays = len(prices)
        maxProfit = 0

        while day < totalDays - 1:

            while day < totalDays - 1 and prices[day] >= prices[day + 1]:
                day += 1

            valley = prices[day]

            while day < totalDays - 1 and prices[day] <= prices[day + 1]:
                day += 1

            peak = prices[day]
            maxProfit += (peak - valley)
        return maxProfit


