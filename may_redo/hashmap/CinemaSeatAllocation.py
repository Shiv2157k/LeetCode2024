from collections import defaultdict
from typing import List


class CinemaSeatAllocation:

    def max_number_of_families(self, n: int, reserved_seats: List[List[int]]) -> int:
        """
        Approach: HashSet and Map
        T: O(K + N) n - no of rows, k - total number of initial reservations
        S: O(R) - rows with blocked seats
        :param n:
        :param reserved_seats:
        :return:
        """

        # Each row has 3 possible group positions: 'left', 'middle', 'right'.
        # We will keep track of which positions are unavailable (blocked).
        blocked = defaultdict(set)

        # Iterate over all reserved seats, saving blocked positions.
        for row, col in reserved_seats:

            if col in (2, 3, 4, 5):
                blocked[row].add('left')
            if col in (4, 5, 6, 7):
                blocked[row].add('middle')
            if col in (6, 7, 8, 9):
                blocked[row].add('right')

        # The variable total will hold the number of 4-person reservations available.
        # Initialize it with 2 per row having no seats blocked.
        total = 2 * (n - len(blocked))
        # Provide the number of sections available based on the number blocked.
        # For example, if 0 are blocked, 2 are available.
        num_available = {0: 2, 1: 1, 2: 1, 3: 0}

        # For each row with blocked sections, add the number of available sections.
        for num_blocked in blocked.values():
            total += num_available[len(num_blocked)]
        return total
