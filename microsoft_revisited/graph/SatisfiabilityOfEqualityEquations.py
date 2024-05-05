from typing import List


class SatisfiabilityOfEqualityEquations:

    def equations_possible(self, equations: List[str]) -> bool:
        """
        Approach: Graph DFS
        T: O(max(N, |E|)) E-> letter size - > O(N)
        S: O(max(N, |E|)) -> O(1)
        :param equations:
        :return:
        """

        # Step 1: Build the graph
        graph: List[List[int]] = [[] for _ in range(26)]
        # 0 1 2 3
        # a = = b
        for equation in equations:

            # note: build graph for only == equations
            if equation[1] == '=':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')

                graph[x].append(y)
                graph[y].append(x)

        # step 2: color the nodes during dfs
        colors: List[int] = [-1] * 26

        # step 4: apply dfs for all the nodes and color respectively
        def dfs(node: int, color: int):

            if colors[node] == -1:
                colors[node] = color
                for neighbor in graph[node]:
                    dfs(neighbor, color)

        # step 3: run the dfs and provide colors
        for i in range(26):
            if colors[i] != -1:
                dfs(i, i)

        # step 5: traverse through the != equations
        for equation in equations:
            if equation[1] == '!':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[1]) - ord('a')

                # our graph nodes are disconnected somewhere
                if colors[x] == colors[y]:
                    return False
        return True
