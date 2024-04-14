from typing import List


class Equations:

    def equationsSatisfy(self, equations: List[str]) -> bool:
        """
        Approach: DFS
        T: O(max(N,∣Σ∣))
        S: O(max(N,∣Σ∣)) -> O(1)
        :param equations:
        :return:
        """

        # Step 1: Build the graph for all 26 characters
        graph = [[] for _ in range(26)]

        for eq in equations:

            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')

                graph[x].append(y)
                graph[y].append(x)

        # Step 2: mark the colors
        colors = [-1] * 26

        def depthFirstSearch(node: int, color):

            if colors[node] == -1:
                colors[node] = color

                for neighbor in graph[node]:
                    depthFirstSearch(neighbor, color)

        for i in range(26):
            depthFirstSearch(i, i)

        for eq in equations:
            if eq[1] == '!':

                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')

                if colors[x] == colors[y]:
                    return False
        return True

    def equationsSatisfyV1(self, equations: List[str]) -> bool:
        """
        Approach: Union Find
        T: O(Nlog∣Σ∣)
        S: O(∣Σ∣) -> O(1)
        :param equations:
        :return:
        """

        root = list(range(26))

        def find(x: int):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x: int, y: int):
            x, y = find(x), find(y)
            root[x] = y

        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)

        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True
