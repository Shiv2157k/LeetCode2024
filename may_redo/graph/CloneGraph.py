from typing import Optional, List
from collections import deque


class Node:

    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:

    def clone_graph_v0(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach:
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """

        if not node:
            return node

        def clone(node: Optional['Node']):
            nonlocal visited

            if not node:
                return node

            if node in visited:
                return visited[node]

            clone_node = Node(node.val, [])
            visited[node] = clone_node

            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))

        visited = {}
        clone(node)
        return visited[node]

    def clone_graph_v1(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach: Iterative (BFS)
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """

        if not node:
            return node

        queue = deque([node])
        visited = {node: Node(node.val, [])}

        while queue:
            curr_node = queue.popleft()

            if curr_node.neighbors:
                for neighbor in curr_node.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val, [])
                        queue.append(neighbor)
                    visited[curr_node].neighbors.append(visited[neighbor])
        return visited[node]
