from collections import deque
from typing import List


class UnionFind:

    def __init__(self, n: int):
        # builds set -> make set for n = 5
        # [ [0], [1], [2], [3], [4]]
        # [0, 1, 2, 3, 4]
        self.parent = [node for node in range(n)]
        # this is for tracking ranks helps
        # in union operation
        self.size = [1] * n

    def find(self, x: int):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            old_root = self.parent[x]
            self.parent[x] = root
            x = old_root
        return root

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True


class Graph:

    def is_valid_tree_v6(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: Union Find
        T: O(N * alpha(N))
        S: O(N)
        :param edges:
        :param n:
        :return:
        """
        if len(edges) == n - 1:
            return False

        unionFind = UnionFind(n)
        for x, y in edges:
            if not unionFind.union(x, y):
                return False
        return True

    def is_valid_tree_v5(self, edges: List[List[int]], n: int) -> bool:
        if len(edges) == n - 1:
            return False

        adjacent_list = self._build_adjacent_list(edges, n)

        queue = deque([0])
        seen = {0}

        while queue:
            node = queue.popleft()
            for neighbor in adjacent_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
        return len(seen) == n

    def is_valid_tree_v4(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: Advanced Recursion BFS
        T: O(N)
        S: O(N)
        :param edges:
        :param n:
        :return:
        """
        if len(edges) == n - 1:
            return False

        adjacent_list = self._build_adjacent_list(edges, n)
        seen = set()

        def dfs(node):

            if node in seen:
                return
            seen.add(node)

            for neighbor in adjacent_list[node]:
                dfs(neighbor)

        dfs(0)
        return len(seen) == n

    def is_valid_tree_v3(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: Advance Iterative BFS
        T: O(N)
        S: O(N)
        :param edges:
        :param n:
        :return:
        """
        if len(edges) == n - 1:
            return False

        adjacent_list = self._build_adjacent_list(edges, n)
        stack = [0]
        seen = {0}

        while stack:
            node = stack.pop()
            for neighbor in adjacent_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)
        return len(seen) == n

    def is_valid_tree_v2(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: BFS
        T: O(N + E)
        S: O(N + E)
        :param edges:
        :param n:
        :return:
        """

        if len(edges) == n - 1:
            return False

        adjacent_list = self._build_adjacent_list(edges, n)
        queue = deque([0])
        parent = {0: -1}

        while queue:
            node = queue.popleft()
            for neighbor in adjacent_list[node]:

                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                queue.append(neighbor)
        return len(parent) == n

    def is_valid_tree_v1(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: DFS Recursion
        T: O(N + E)
        S: O(N + E)
        :param edges:
        :param n:
        :return:
        """

        if len(edges) == n - 1:
            return False

        adjacent_list = self._build_adjacent_list(edges, n)

        seen = set()

        def dfs(node: int, parent: int):
            if node in seen:
                return
            seen.add(node)

            for neighbor in adjacent_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                result = dfs(neighbor, node)
                if not result:
                    return False
            return True

        return dfs(0, -1) and len(seen) == n

    def is_valid_tree_v0(self, edges: List[List[int]], n: int) -> bool:
        """
        Approach: DFS Iterative
        T: O(V + E)
        S: O(V + E)
        :param edges:
        :param n:
        :return:
        """

        if len(edges) != n - 1:
            return False

        adjacentList = self._build_adjacent_list(edges, n)

        stack = [0]
        parent = {0: -1}

        while stack:

            node = stack.pop()

            for neighbor in adjacentList[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                stack.append(neighbor)
                parent[neighbor] = node
        return len(parent) == n

    def _build_adjacent_list(self, edges: List[List[int]], n) -> List[List[int]]:
        adjacentList = [[] for _ in range(n)]
        for e1, e2 in edges:
            adjacentList[e1].append(e2)
            adjacentList[e2].append(e1)
        return adjacentList


if __name__ == "__main__":
    graph = Graph()
    print(graph.is_valid_tree_v0([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v0([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v1([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v1([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v2([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v2([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v3([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v3([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v4([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v4([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v5([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v5([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
    print(graph.is_valid_tree_v6([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
    print(graph.is_valid_tree_v6([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
    print("__**__")
