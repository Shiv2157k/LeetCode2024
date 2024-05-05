from typing import List


class GraphBiPartite:

    def is_bipartite(self, graph: List[List[int]]) -> bool:
        """
        Approach: DFS with stack
        T: O(N + E)
        S: O(N)
        :param graph:
        :return:
        """
        color = {}

        for node in range(len(graph)):

            if node not in color:
                color[node] = 0
                stack = [node]
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = 1 ^ color[node]
                        elif color[neighbor] == color[node]:
                            return False
        return True
