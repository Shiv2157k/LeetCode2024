from collections import deque
from typing import List


class StonesOverGrid:

    def minimum_moves_to_spread(self, grid: List[List[int]]):
        """
        Approach: Breadth First Search
        T: O(9!)
        S: O(9!)
        :param grid:
        :return:
        """
        rows = len(grid)
        cols = len(grid[0])
        start_state = []
        # Step 1: build the start state
        for row in range(rows):
            for col in range(cols):
                start_state.append(grid[row][col])

        # mark this state in visited
        # since it is take lot of place to store lists in the set
        # better idea is to hash the list
        visited = {self._generate_hash(start_state)}
        target_state = (1, 1, 1, 1, 1, 1, 1, 1, 1)

        queue = deque()
        # add it into the queue for processing
        queue.append(start_state)
        moves = 0
        n = 9

        # traverse through the queue
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_state = queue.popleft()
                # check if we have reached the target state
                if tuple(curr_state) == target_state:
                    return moves

                for cell in range(n):

                    if curr_state[cell] > 1:

                        for next_cell in self._adjacent_cells(cell):
                            new_state = curr_state[:]

                            new_state[cell] -= 1
                            new_state[next_cell] += 1

                            hash_val = self._generate_hash(new_state)

                            if hash_val not in visited:
                                visited.add(hash_val)
                                queue.append(new_state)
            moves += 1
        return -1

    def _adjacent_cells(self, cell: int) -> List[int]:
        # offset
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        row = cell // 3
        col = cell % 3
        adjacent_cells = []

        for direction in directions:
            dr = row + direction[0]
            dc = col + direction[1]
            if 0 <= dr < 3 and 0 <= dc < 3:
                adjacent_cells.append(dr * 3 + dc)
        return adjacent_cells

    def _generate_hash(self, state: List[int]) -> int:
        prime = 31
        hash_val = 1
        for num in state:
            hash_val = hash_val * prime + num
        return hash_val
