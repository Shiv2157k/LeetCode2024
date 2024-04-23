from typing import List
from collections import deque


class MinimumGeneticMutation:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Approach: BFS
        T: O(B) -> B is bank length  O(nB+m^n⋅n^2⋅m)
        S: O(1) -> O(nB + m ^ n)
        :param startGene:
        :param endGene:
        :param bank:
        :return:
        """

        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:

            node, steps = queue.popleft()

            if node == endGene:
                return steps

            for char in 'ACGT':
                for i in range(len(node)):
                    neighbor = node[:i] + char + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)
        return -1
