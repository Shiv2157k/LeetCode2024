from collections import deque


class Knight:

    def minKnightMovesV2(self, x: int, y: int) -> int:
        """
        Approach: BFS with pruning
        T: O(|x|*|y|)
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
                """
                The symmetry is part of it (meaning that reaching (x, y), (-x, y), (x, -y), (-x, -y) 
                all require the same number of moves). 
                Also, the moves ((-1, -2) and (-2, -1)) only go in the negative direction, 
                and the author is bounding the search space to be -1 to abs(x) +2 for x direction 
                and -1 to abs(y) + 2 in y direction. So the search space is bounded to the 
                positive x, positive y quadrant
                """
                if (dx, dy) not in visited and -1 <= dx <= x + 2 and -1 <= dy <= y + 2:
                    visited.add((dx, dy))
                    queue.append((dx, dy, steps + 1))
        return -1

    def minimum_moves_v1(self, x: int, y: int) -> int:
        """
        Approach: BFS Bi Direction Search
        T: O((max(|x|, |y|))^2)
        S: O((max(|x|, |y|))^2)
        :param x:
        :param y:
        :return:
        """

        directions = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1))
        origin_queue = deque([(0, 0, 0)])
        origin_visited = {(0, 0): 0}

        target_queue = deque([(x, y, 0)])
        target_visited = {(x, y): 0}

        while True:

            origin_x, origin_y, origin_steps = origin_queue.popleft()

            if (origin_x, origin_y) in target_visited:
                return target_visited[(origin_x, origin_y)] + origin_steps

            target_x, target_y, target_steps = target_queue.popleft()

            if (target_x, target_y) in origin_visited:
                return origin_visited[(target_x, target_y)] + target_steps

            for direction in directions:
                dx_origin = origin_x + direction[0]
                dy_origin = origin_y + direction[1]
                origin_steps += 1

                if (dx_origin, dy_origin) not in origin_visited:
                    origin_visited[(dx_origin, dy_origin)] = origin_steps
                    origin_queue.append((dx_origin, dy_origin, origin_steps + 1))

                dx_target = target_x + direction[0]
                dy_target = target_y + direction[1]
                target_steps += 1

                if (dx_target, dy_target) not in target_visited:
                    target_visited[(dx_target, dy_target)] = target_steps
                    target_queue.append((dx_target, dy_target, target_steps + 1))

    def minimum_moves_v0(self, x: int, y: int) -> int:
        """
        Approach: BFS Single Direction
        T: O((max(|x|, |y|))^2)
        S: O((max(|x|, |y|))^2)
        :param x:
        :param y:
        :return:
        """
        directions = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1))
        queue = deque([(0, 0)])
        steps = 0
        visited = set()
        visited.add((0, 0))

        while queue:
            level = len(queue)
            for _ in range(level):
                x_, y_ = queue.popleft()
                if (x_, y_) == (x, y):
                    return steps
                for direction in directions:
                    dx = x_ + direction[0]
                    dy = y_ + direction[1]

                    if (dx, dy) not in visited:
                        visited.add((dx, dy))
                        queue.append((dx, dy))
            steps += 1
        return steps
