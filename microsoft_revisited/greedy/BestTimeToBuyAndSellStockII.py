from typing import List



class BestTimeToBuyAndSellStocksII:


    def maxProfitV1(self, prices: List[int]) -> int:
        """
        Approach: Greedy
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

    def maxProfitV0(self, prices: List[int]) -> int:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        ptr = 0
        maxProfit = 0

        while ptr < len(prices) - 1:

            while ptr < len(prices) and prices[ptr] >= prices[ptr + 1]:
                ptr += 1
            valley = prices[ptr]

            while ptr < len(prices) and prices[ptr] <= prices[ptr + 1]:
                ptr += 1

            peak = prices[ptr]
            maxProfit += peak - valley
        return maxProfit