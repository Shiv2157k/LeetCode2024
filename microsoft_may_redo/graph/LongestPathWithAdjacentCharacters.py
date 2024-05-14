from typing import List


class LongestPathWithAdjacentCharacters:

    def longest_path(self, parent: List[int], s: str) -> int:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param parent:
        :param s:
        :return:
        """

        # Step 1: build graph
        graph = {}

        for i in range(len(parent)):
            graph[i] = graph.get(i, [])
            graph[i].append(parent[i])

            graph[parent[i]] = graph.get(parent[i], [])
            graph[parent[i]].append(i)

        longest_path = 0

        # dfs
        def helper(curr_node: int, parent: int):
            nonlocal longest_path

            first_longest = 0
            second_longest = 0

            for child in graph[curr_node]:

                if child != parent:

                    child_path = helper(child, curr_node)

                    if s[child] != s[curr_node]:

                        if child_path > second_longest:
                            second_longest = child_path

                        if second_longest > first_longest:
                            first_longest, second_longest = second_longest, first_longest

            case1 = max(first_longest, second_longest) + 1
            case2 = 1
            case3 = 1 + first_longest + second_longest

            longest_path = max(longest_path, case1, case2, case3)
            return max(case1, case2)

        helper(0, -1)
        return longest_path
