from typing import List, Dict
from math import inf


class OptimalAccountBalancing:

    def __init__(self):
        self.__balance_list = []

    def min_transfer_v0(self, transactions: List[List[int]]) -> int:
        """
        Approach: Backtracking
        T: O((N - 1)!)
        S: O(N)
        :param transactions:
        :return:
        """
        person_credit = {}

        for p1, p2, amount in transactions:
            person_credit[p1] = person_credit.get(p1, 0) + amount
            person_credit[p2] = person_credit.get(p2, 0) - amount

        for person, amount in person_credit.items():
            if amount != 0:
                self.__balance_list.append(amount)

        n = len(self.__balance_list)
        return self.__backtrack(0, n)

    def __backtrack(self, curr: int, size: int):

        while curr < size and self.__balance_list[curr] == 0:
            curr += 1

        if curr == size:
            return 0

        cost = inf

        for next_pos in range(curr + 1, size):
            if self.__balance_list[next_pos] * self.__balance_list[curr] < 0:
                self.__balance_list[next_pos] += self.__balance_list[curr]
                cost = min(cost, 1 + self.__backtrack(curr + 1, size))
                self.__balance_list[next_pos] -= self.__balance_list[curr]
        return cost

    def min_transfer_v1(self, transactions: List[List[int]]) -> int:
        """
        Approach: DP
        T: O(N * 2^N)
        S: O(2^N)
        :param transactions:
        :return:
        """
        self._balance_list: List[int] = []
        credit_list: Dict[int, int] = {}

        for p1, p2, amount in transactions:
            credit_list[p1] = credit_list.get(p1, 0) + amount
            credit_list[p2] = credit_list.get(p2, 0) - amount

        for amount in credit_list.values():
            if amount != 0:
                self._balance_list.append(amount)

        N = len(self._balance_list)
        dp = [0] * (2 ** N)
        sums = [0] * (2 ** N)

        for mask in range(2 ** N):
            set_bit = 1
            for b in range(N):

                if mask & set_bit == 0:
                    nxt = mask | set_bit
                    sums[nxt] = sums[mask] + self._balance_list[b]
                    if sums[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[mask] + 1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[mask])
                set_bit <<= 1
        return N - dp[-1]