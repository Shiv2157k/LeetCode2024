from typing import List


class HouseRobberII:

    def total_money_v1(self, houses: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param houses:
        :return:
        """
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]

        return max(self._robbed_house(houses[:-1]), self._robbed_house(houses[1:]))

    def _robbed_house(self, houses: List[int]) -> int:
        robber1 = 0
        robber2 = 0
        for house in houses:
            temp = robber1
            robber1 = max(robber2 + house, robber1)
            robber2 = temp
        return robber1

    def total_money_v0(self, houses: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param houses:
        :return:
        """

        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses)

        return max(self._rob_house(houses, 0, len(houses) - 1), self._rob_house(houses, 1, len(houses)))

    def _rob_house(self, houses: List[int], start: int, end: int) -> int:
        dp = [0] * (end - start)
        dp[0] = houses[start]
        dp[1] = max(houses[start + 1], dp[0])

        for curr_house in range(start + 2, end):
            dp[curr_house - start] = max(dp[curr_house - start - 2] + houses[curr_house], dp[curr_house - start - 1])
        return dp[-1]


if __name__ == "__main__":
    robber = HouseRobberII()
    print(robber.total_money_v0([1, 2, 3, 1]))
    print(robber.total_money_v0([1, 2, 3]))

    print(robber.total_money_v1([1, 2, 3, 1]))
    print(robber.total_money_v1([1, 2, 3]))