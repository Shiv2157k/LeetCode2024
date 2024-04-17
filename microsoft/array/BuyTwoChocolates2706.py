from typing import List


class Chocolates:

    def buyChoco(self, prices: List[int], money: int) -> int:
        """
        Approach: One Pass
        T: O((N)
        S: O(1)
        :param prices:
        :param money:
        :return:
        """
        if len(prices) < 2:
            return money
        firstMin = min(prices[0], prices[1])
        secondMin = max(prices[0], prices[1])

        for i in range(2, len(prices)):

            if prices[i] < firstMin:
                secondMin = firstMin
                firstMin = prices[i]
            elif prices[i] < secondMin:
                secondMin = prices[i]
        if firstMin + secondMin <= money:
            return money - firstMin + secondMin
        else:
            return money
