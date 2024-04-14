from typing import List


class OptimalAccountBalancing:

    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        Approach: BackTrack
        T: O(N - 1)!
        S: O(N)
        :param transactions:
        :return:
        """

        # Step 1: build the net amount balance of each person
        balanceMap = {}
        for fromPerson, toPerson, amount in transactions:
            balanceMap[fromPerson] = balanceMap.get(fromPerson, 0) + amount
            balanceMap[toPerson] = balanceMap.get(toPerson, 0) - amount

        # Step 2: Store the amount which are not equals to zero
        creditList = []
        for amount in balanceMap.values():
            if amount != 0:
                creditList.append(amount)

        n = len(creditList)
        # Step 3: Back track until all the amounts are settled i.e., zero
        return self._backTrack(0, n, creditList)

    def _backTrack(self, curr: int, total: int, creditList: List[int]):

        # base case
        while curr < total and creditList[curr] == 0:
            curr += 1

        if curr == total:
            return 0

        cost = float("inf")

        for next in range(curr + 1, total):

            if creditList[next] * creditList[curr] < 0:
                creditList[next] = creditList[next] + creditList[curr]
                cost = min(cost, 1 + self._backTrack(curr + 1, total, creditList))
                creditList[next] = creditList[next] - creditList[curr]
        return cost


if __name__ == "__main__":
    optimalAccountBalancing = OptimalAccountBalancing()
    print(optimalAccountBalancing.minTransfers([[0, 1, 10], [2, 0, 5]]))
    print(optimalAccountBalancing.minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
