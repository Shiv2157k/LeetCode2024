from collections import deque


class MinimumKnightMoves:

    def min_knight_moves(self, x: int, y: int) -> int:
        """
        Approach: BFS with pruning searching just positive quadrant
        T: O(x * y)
        S: O(x * y)
        :param x:
        :param y:
        :return:
        """

        directions = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1))

        visited = set()
        queue = deque([(0, 0, 0)])
        x, y = abs(x), abs(y)

        while queue:

            curr_x, curr_y, steps = queue.popleft()

            if (curr_x, curr_y) == (x, y):
                return steps

            for direction in directions:
                dx = curr_x + direction[0]
                dy = curr_y + direction[1]
                # condition -1 <= (dx or dy) < (x or y) + 2 to make sure search space is bounded to only
                # positive x and positive y qudrant
                if (dx, dy) not in visited and -1 <= dx <= x + 2 and -1 <= dy <= y + 2:
                    visited.add((dx, dy))
                    queue.append((dx, dy, steps + 1))
        return -1
