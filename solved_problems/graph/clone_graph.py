from collections import deque
from typing import Optional


class GraphNode:

    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


class Graph:

    def __init__(self):
        self._visited = {}

    def clone_v0(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        """
        Approach: DFS
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """

        if not node:
            return node
        if node in self._visited:
            return self._visited[node]

        clone_node = GraphNode(node.val, [])
        self._visited[node] = clone_node

        if node.neighbors:
            for next_node in node.neighbors:
                # if next_node not in self._visited:
                clone_node.neighbors.append(self.clone_v0(next_node))
        return clone_node

    def clone_v1(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        """
        Approach: BFS
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """
        if not node:
            return node
        self._visited = {}
        queue = deque
        queue.append(node)
        clone_node = GraphNode(node.val, [])
        self._visited[node] = clone_node

        while queue:
            curr_node = queue.popleft()
            # if curr_node.neighbors:
            for next_node in curr_node.neighbors:
                if next_node not in self._visited:
                    self._visited[next_node] = GraphNode(next_node.val, [])
                    queue.append(next_node)
                self._visited[curr_node].neighbors.append(self._visited[next_node])
        return self._visited[node]

