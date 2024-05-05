from typing import List, Set


class Trees:

    def find_min_height_trees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Approach: BFS Topological Sort
        T: O(N)
        S: O(N)
        :param n:
        :param edges:
        :return:
        """

        if n == 1:
            return [0]

        neighbors: List[Set[int]] = [set() for _ in range(n)]
        # Step 1: Build the adjacency list
        for e1, e2 in edges:
            neighbors[e1].append(e2)
            neighbors[e2].append(e1)

        # add all the leaf nodes
        leaves: List[int] = []
        for node in range(n):
            # if the in-degree is one
            if len(neighbors[node]) == 1:
                leaves.append(node)

        # traverse until we have two nodes left
        while n > 2:
            # as we are iterating over leaf nodes
            # subtract leafs from total nodes
            n -= len(leaves)
            new_leaves: List[int] = []
            for node in leaves:
                # we are branching out/ cutting off the leafs
                next_node = neighbors[node].pop()
                neighbors[next_node].remove(node)
                if len(neighbors[next_node]) == 1:
                    new_leaves.append(next_node)
            # next level of leafs will be processed
            leaves = new_leaves
        return leaves
