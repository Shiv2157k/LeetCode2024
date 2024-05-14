from typing import List


class SatisfiabilityOfEqualityEquations:

    def equation_possible(self, equations: List[str]) -> bool:
        """
        Approach: Graph DFS
        T: O(max(N, |E|)) E -> 26 -> O(N)
        S: O(max(N, |E|)) -> O(N)
        :param equations:
        :return:
        """

        # Step 1: Build a graph for equations that are equal
        graph = [[] for _ in range(26)]

        for equation in equations:
            if equation[1] == '=':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        # Step 2:
        # initialize a bucket of size 26 with -1
        color_bucket = [-1] * 26

        def dfs(node, color):
            if color == -1:
                color_bucket[node] = color
                for neighbor in graph[node]:
                    dfs(neighbor, color)

        # iterate through if its -1 and apply dfs to color all
        for i in range(26):
            if color_bucket[i] == -1:
                dfs(i, i)

        # Step 3: Traverse through equations with != and check the colors
        # if there is same colors exists b/w a and b in a!=b then it is not satisfied
        for equation in equations:
            if equation[1] == '!':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')

                if color_bucket[x] == color_bucket[y]:
                    return False
        return True
