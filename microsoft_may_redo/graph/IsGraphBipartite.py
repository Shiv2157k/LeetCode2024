from typing import List


class GraphBipartite:

    def is_graph_bipartite(self, graph: List[List[int]]) -> bool:
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
                    curr_node = stack.pop()

                    for next_node in graph[curr_node]:
                        if next_node not in color:
                            stack.append(next_node)
                            color[next_node] = 1 ^ color[curr_node]
                        elif color[curr_node] == color[next_node]:
                            return False
        return True
