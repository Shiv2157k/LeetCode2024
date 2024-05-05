from typing import List, Deque, Set
from collections import deque


class SpreadStonesOverGrid:

    def minimum_moves_to_make_all_ones(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        T: O(N * M)
        S: O(N * M)
        :param grid:
        :return:
        """

        start_state: List[int] = []

        for row in range(3):
            for col in range(3):
                start_state.append(grid[row][col])

        queue: Deque[List[int]] = deque([start_state])
        visited: Set[int] = set()
        visited.add(self._generate_hash(start_state))
        target_state: List[int] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        moves: int = 0

        while queue:

            size = len(queue)

            for level in range(size):

                curr_state = queue.popleft()
                if curr_state == target_state:
                    return moves

                for cell in range(9):

                    if curr_state[cell] > 1:
                        for next_cell in self._build_adjacent_cells(cell):

                            new_state = curr_state.copy()

                            new_state[cell] -= 1
                            new_state[next_cell] += 1

                            hash_val = self._generate_hash(new_state)

                            if hash_val not in visited:
                                visited.add(hash_val)
                                queue.append(new_state)
            moves += 1
        return -1

    def _build_adjacent_cells(self, index: int) -> List[int]:
        adjacent_cells: List[int] = []
        row = index // 3
        col = index % 3

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for direction in directions:
            dr = row + direction[0]
            dc = row + direction[1]
            if 0 <= dr < 3 and 0 <= dc < 3:
                adjacent_cells.append(dr * 3 + dc)
        return adjacent_cells

    def _generate_hash(self, start_state: List[int]) -> int:
        prime: int = 31
        hash_val = 1
        for num in start_state:
            hash_val = hash_val * prime + num
        return hash_val
