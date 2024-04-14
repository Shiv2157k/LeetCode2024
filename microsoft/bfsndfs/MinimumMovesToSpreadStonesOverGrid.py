from collections import deque
from typing import List


class SpreadStones:

    def minimumMoveToSpreadEven(self, grid: List[List[int]]) -> int:

        startState = []

        for row in range(3):
            for col in range(3):
                startState.append(grid[row][col])

        queue = deque([startState])
        visited = set()
        visited.add(self._generateHash(startState))
        targetState = (1, 1, 1, 1, 1, 1, 1, 1, 1)
        moves = 0

        while queue:

            size = len(queue)

            for level in range(size):

                currState = queue.popleft()

                if currState == targetState:
                    return moves

                for cell in range(9):

                    if currState[cell] > 1:

                        for nextCell in self._adjacentCell(cell):

                            newState = currState.copy()

                            newState[cell] -= 1
                            newState[nextCell] += 1

                            hashVal = self._generateHash(newState)

                            if hashVal not in visited:
                                visited.add(hashVal)
                                queue.append(newState)
            moves += 1
        return -1

    def _adjacentCell(self, index: int):

        adjacentList = []
        row = index // 3
        col = index % 3

        if col > 0:
            adjacentList.append(index - 1)  # left
        if col < 2:
            adjacentList.append(index + 1)  # right
        if row > 0:
            adjacentList.append(index - 3)  # up
        if row < 2:
            adjacentList.append(index + 3)  # down
        return adjacentList

    def _generateHash(self, state: List[int]):
        prime = 31
        hash = 1
        for num in state:
            hash = hash * prime + num
        return hash
