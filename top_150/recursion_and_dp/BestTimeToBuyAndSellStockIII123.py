from typing import List


class BuyAndSellStock:

    def maxProfitV0(self, prices: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param prices:
        :return:
        """

        if len(prices) <= 1:
            return 0

        leftMin, rightMax = prices[0], prices[-1]
        length = len(prices)

        leftProfits = [0] * length
        rightProfits = [0] * (length + 1)

        for left in range(1, length):

            leftProfits[left] = max(leftProfits[left], prices[left] - leftMin)
            leftMin = min(leftMin, prices[left])

            right = length - left - 1

            rightProfits[right] = max(rightProfits[right + 1], rightMax - prices[right])
            rightMax = max(rightMax, prices[right])

        maxProfit = 0
        for i in range(length):
            maxProfit = max(maxProfit, leftProfits[i] + rightProfits[i + 1])
        return maxProfit

    def maxProfitV1(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        t1Cost, t2Cost = float("inf"), float("inf")
        t1Profit, t2Profit = 0, 0

        for price in prices:

            t1Cost = min(t1Cost, price)
            t1Profit = max(t1Profit, price - t1Cost)

            t2Cost = min(t2Cost, price - t1Profit)
            t2Profit = max(t2Profit, price - t2Cost)
        return t2Profit
