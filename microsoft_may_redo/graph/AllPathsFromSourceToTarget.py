from typing import List


class AllPathsFromSourceToTarget:

    def all_paths_from_source_to_target(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Approach: Backtracking
        T: O(2^N * N)
        S: O(N)
        :param graph:
        :return:
        """

        target_node = len(graph) - 1
        results = []

        def backtrack(curr_node: int, path: List[int]) -> None:
            if curr_node == target_node:
                results.append(list(path))
                return

            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        backtrack(0, [0])
        return results