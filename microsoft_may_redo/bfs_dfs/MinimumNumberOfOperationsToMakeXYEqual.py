from collections import deque


class XAndY:

    def minimum_operations_to_make_it_equal(self, x: int, y: int) -> int:
        """
        Approach: BFS
        T: O(y - x)
        S: O(y - x)
        :param x:
        :param y:
        :return:
        """

        # validation
        if y >= x:
            return y - x

        queue = deque([(0, x)])
        visited = {x}

        while queue:

            min_operations, curr_x = queue.popleft()

            if curr_x == y:
                return min_operations
            # note we check curr_x mod by 11 and add currx div by 11
            if curr_x % 11 == 0 and curr_x // 11 not in visited:
                queue.append((min_operations + 1, curr_x // 11))
                visited.add(curr_x // 11)
            if curr_x % 5 == 0 and curr_x // 5 not in visited:
                queue.append((min_operations + 1, curr_x // 5))
                visited.add(curr_x // 5)
            if curr_x - 1 not in visited:
                queue.append((min_operations + 1, curr_x - 1))
                visited.add(curr_x - 1)
            if curr_x + 1 not in visited:
                queue.append((min_operations + 1, curr_x + 1))
                visited.add(curr_x + 1)
