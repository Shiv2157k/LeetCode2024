from typing import List


class UniDirectedGraph:

    def number_of_connected_components(self, edges: List[List[int]], n: int) -> int:
        """
        Approach: DFS
        T: O(E + V)
        S: O(E + V)
        :param edges:
        :return:
        """

        adjacent_list = {}
        visited = set()
        counter = 0

        for node1, node2 in edges:
            adjacent_list[node1] = adjacent_list.get(node1, [])
            adjacent_list[node1].append(node2)
            adjacent_list[node2] = adjacent_list.get(node2, [])
            adjacent_list[node2].append(node1)

        def dfs(visited, start_node):
            visited.add(start_node)

            if start_node in adjacent_list:
                for next_node in adjacent_list[start_node]:
                    if next_node not in visited:
                        dfs(visited, next_node)

        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(visited, node)
        return counter


if __name__ == "__main__":
    uni_directed_graph = UniDirectedGraph()
    print(uni_directed_graph.number_of_connected_components([[0, 1], [1, 2], [3, 4]], 5))
