from typing import List, Deque, Set, Tuple
from collections import deque


class MinimumGeneticMutation:

    def minMutation(self, start_gene: str, end_gene: str, bank: List[str]) -> int:
        """
        Approach: BFS
        T: O(B) -> B is bank length  O(nB+m^n⋅n^2⋅m)
        S: O(1) -> O(nB + m ^ n)
        :param startGene:
        :param endGene:
        :param bank:
        :return:
        """

        queue: Deque[Tuple[str, int]] = deque([(start_gene, 0)])
        seen: Set = {start_gene}

        while queue:
            curr_gene, steps = queue.popleft()

            if curr_gene == end_gene:
                return steps

            for mutation in ('A', 'C', 'G', 'T'):
                for pos in range(len(curr_gene)):
                    next_gene = curr_gene[:pos] + mutation + curr_gene[pos + 1:]
                    if next_gene not in seen and next_gene in bank:
                        queue.append((next_gene, steps + 1))
                        seen.add(next_gene)
        return -1

