from typing import Optional
from collections import deque


class Node:

    def __init__(self, val: int = -1, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class CloneGraph:

    def __init__(self):
        self.seen = {}

    def cloneV1(self, node: Optional[Node]):
        """
        Approach: BFS
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """
        if not node:
            return node

        visited = {node: Node(node.val, [])}
        queue = deque([node, ])

        while queue:

            currNode = queue.pop()

            if currNode.neighbors:
                for nextNode in currNode.neighbors:
                    if nextNode not in visited:
                        visited[currNode] = Node(nextNode.val, [])
                        queue.append(nextNode)
                    visited[currNode].neighbors.append(visited[node])
        return visited[node]

    def cloneV1(self, node: Optional[Node]):
        """
        Approach: DFS
        T: O(N + M)
        S: O(N)
        :param node:
        :return:
        """
        if not node:
            return node

        if node in self.seen:
            return self.seen[node]

        cloneNode = Node(node.val, [])

        self.seen[node] = cloneNode

        if node.neighbors:
            for nextNode in node.neighbors:
                cloneNode.neighbors.append(self.cloneV1(nextNode))
        return cloneNode