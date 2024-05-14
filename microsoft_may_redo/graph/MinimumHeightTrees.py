from typing import List


class MinimumHeightTrees:

    def find_minimum_height_trees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Approach: Topological Sort (Trimming down leaf nodes)
        T: O(|V|)
        S: O(|V|)
        :param n:
        :param edges:
        :return:
        """

        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]

        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)

        leaves = []
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                next_node = graph[node].pop()
                graph[next_node].remove(node)
                if len(graph[next_node]) == 1:
                    new_leaves.append(next_node)
            leaves = new_leaves
        return leaves
