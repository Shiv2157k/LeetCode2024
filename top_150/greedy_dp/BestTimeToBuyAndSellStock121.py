from typing import List


class BuyStock:

    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """

        minPrice = prices[0]
        maxProfit = 0

        for day in range(1, len(prices)):

            if prices[day] < minPrice:
                minPrice = prices[day]
            if prices[day] - minPrice > maxProfit:
                maxProfit = prices[day] - minPrice
        return maxProfit


if __name__ == "__main__":
    buyStock = BuyStock()
    print(buyStock.maxProfit([7, 1, 5, 3, 6, 4]))
    print(buyStock.maxProfit([7, 6, 4, 3, 1]))
