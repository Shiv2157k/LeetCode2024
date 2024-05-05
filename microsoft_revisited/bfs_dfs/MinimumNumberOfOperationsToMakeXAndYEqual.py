from collections import deque
from typing import Deque, Set, Tuple


class XAndYEqual:

    def minimum_operations(self, x: int, y: int) -> int:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param x:
        :param y:
        :return:
        """

        if y >= x:
            return y - x

        seen: Set = {x}
        queue: Deque[Tuple[int, int]] = deque([(0, x)])

        while queue:
            operations, n = queue.popleft()

            if n == y:
                return operations

            if n % 11 == 0 and n // 11 not in seen:
                queue.append((operations + 1, n // 11))
                seen.add(n // 11)
            if n % 5 == 0 and n // 5 not in seen:
                queue.append((operations + 1, n // 5))
                seen.add(n // 5)
            if n - 1 not in seen:
                queue.append((operations + 1, n - 1))
                seen.add(n - 1)
            if n + 1 not in seen:
                queue.append((operations + 1, n + 1))
                seen.add(n + 1)
