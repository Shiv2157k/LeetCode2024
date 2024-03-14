from collections import deque
from typing import List


class AcyclicGraph:

    def get_all_ancestors(self, n: int, edges:List[List[int]]) -> List[List[int]]:
        """
        Approach: Kahn's Topological Sort Algorithm
        T: O(V + E + V log V)
        S: O(V * E)
        :param n:
        :param edges:
        :return:
        """
        graph = [[] for _ in range(n)]
        ans = [set() for _ in range(n)]
        in_degree = [0] * n

        for parent, child in edges:
            graph[parent].append(child)
            # you can also add direct parent-child link here
            # ans[child].add(parent)
            in_degree[child] += 1

        queue = deque()

        # add the first level of indegree = 0
        for node in range(n):
            if in_degree[node] == 0:
                queue.append(node)

        # perform topological sort
        while queue:
            curr_node = queue.popleft()
            for neighbor in graph[curr_node]:
                # this will be the direct parents
                ans[neighbor].add(curr_node)
                # we are doing this as these will be our ancestors
                ans[neighbor].update(ans[curr_node])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(ancestor) for ancestor in ans]


if __name__ == "__main__":
    acyclic_graph = AcyclicGraph()
    print(acyclic_graph.get_all_ancestors(
        8,
        [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    ))


