from typing import List, Dict


class DifferentAdjacentCharacters:

    def longest_path(self, parent: List[int], s: str) -> int:
        """
        Approach: DFS
        T: O(m + n)
        S: O(m + n)
        :param parent:
        :param s:
        :return:
        """

        # build the graph
        graph: Dict[int, List[int]] = {}

        for i in range(len(parent)):
            graph[i] = graph.get(i, [])
            graph[i].append(parent[i])

            graph[parent[i]] = graph.get(parent[i], [])
            graph[parent[i]].append(i)

        result = 0

        def dfs(curr_node: int, parent: int):
            nonlocal result
            longest = 0
            second_longest = 0

            for child in graph[curr_node]:

                if child != parent and s[child] != s[curr_node]:

                    child_longest = dfs(child, curr_node)

                    if child_longest > second_longest:
                        second_longest = child_longest

                    if second_longest > longest:
                        second_longest, longest = longest, second_longest

            case1 = longest + second_longest + 1
            case2 = 1
            case3 = max(longest, second_longest) + 1
            result = max(result, case1, case2, case3)

            return max(case2, case3)

        dfs(0, -1)

        return result
