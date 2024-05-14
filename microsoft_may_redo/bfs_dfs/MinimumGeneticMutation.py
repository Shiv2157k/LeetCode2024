from typing import List
from collections import deque


class GeneticMutation:

    def minimum_mutation(self, start_gene: str, end_gene: str, bank: List[str]) -> int:
        """
        Approach: Breadth First Search
        T: O(B)
        S: O(1)
        :param start_gene:
        :param end_gene:
        :param bank:
        :return:
        """

        queue = deque([(start_gene, 0)])
        seen = {start_gene}

        while queue:

            curr_gene, min_mutation = queue.popleft()

            if curr_gene == end_gene:
                return min_mutation

            for mutation in ('A', 'C', 'G', 'T'):

                for pos in range(len(curr_gene)):
                    next_gene = curr_gene[:pos] + mutation + curr_gene[pos + 1:]

                    if next_gene in bank and next_gene not in seen:
                        queue.append((next_gene, min_mutation + 1))
                        seen.add(next_gene)
        return -1
