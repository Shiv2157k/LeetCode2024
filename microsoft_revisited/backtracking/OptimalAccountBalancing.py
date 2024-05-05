from typing import List, Dict
from math import inf


class OptimalAccountBalancing:

    def __init__(self):
        self._balances: List[int] = []

    def min_transfers(self, transactions: List[List[int]]) -> int:

        # calculate the debit or credit of each person
        person_credit_debit_map: Dict[int, int] = {}

        for person1, person2, amount in transactions:
            person_credit_debit_map[person1] = person_credit_debit_map.get(person1, 0) + amount
            person_credit_debit_map[person2] = person_credit_debit_map.get(person2, 0) - amount

        # add all the credit, debit of a person which are not zero into balances list
        for amount in person_credit_debit_map.values():
            if amount != 0:
                self._balances.append(amount)

        # call the back track to determine how many transfers needed
        # total non-zero debit credit amounts
        n = len(self._balances)
        return self._back_track(0, n)

    def _back_track(self, ptr: int, n: int) -> int:

        # to determine zeros
        while ptr < n and self._balances[ptr] == 0:
            ptr += 1

        # base case
        if ptr == n:
            return 0

        min_transfers = inf

        for next_ptr in range(ptr + 1, n):
            # if one is negative and the other is positive
            if self._balances[next_ptr] * self._balances[ptr] < 0:
                self._balances[next_ptr] = self._balances[next_ptr] + self._balances[ptr]
                min_transfers = min(min_transfers, 1 + self._back_track(ptr + 1, n))
                self._balances[next_ptr] = self._balances[next_ptr] - self._balances[ptr]
        return min_transfers
