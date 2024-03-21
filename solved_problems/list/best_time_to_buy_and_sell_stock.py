from typing import List


class Stocks:

    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param prices:
        :return:
        """
        min_price = prices[0]
        max_profit = 0

        for day in range(1, len(prices)):
            if min_price > prices[day]:
                min_price = prices[day]
            if max_profit < prices[day] - min_price:
                max_profit = prices[day] - min_price
        return max_profit


if __name__ == "__main__":
    stocks = Stocks()
    print(stocks.max_profit([7, 1, 5, 3, 6, 4]))