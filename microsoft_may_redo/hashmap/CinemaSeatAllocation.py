from typing import List, Set, Dict


class CinemaSeatsAllocation:

    def max_number_of_families(self, n: int, reserved_seats: List[List[int]]) -> int:
        """
        Approach: Hash Map and Sets
        T: O(r + n)
        S: O(r)
        :param n:
        :param reserved_seats:
        :return:
        """

        blocked: Dict[int, Set] = {}
        """
            X             X                 X 
        1   2   3|   |4   5   6   7|   |8   9   10
        # left - l
        # middle - m
        # right - m
        """

        for row, seat in reserved_seats:
            if seat in (2, 3, 4, 5):
                blocked[row] = blocked.get(row, set())
                blocked[row].add('l')
            if seat in (4, 5, 6, 7):
                blocked[row] = blocked.get(row, set())
                blocked[row].add('m')
            if seat in (6, 7, 8, 9):
                blocked[row] = blocked.get(row, set())
                blocked[row].add('r')

        total_seats = 2 * (n - len(blocked))

        seat_allocation = {0: 2, 1: 1, 2: 1, 3: 0}

        for blocked_seats in blocked.values():
            total_seats += seat_allocation[len(blocked_seats)]
        return total_seats
