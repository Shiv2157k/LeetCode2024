from typing import List


class SatisfiabilityOfEqualityEquations:

    def equations_possible(self, equations: List[str]) -> bool:
        """
        Approach: Union Find
        T: O(N log |E|)
        S: O(|E|) -> O(1)
        :param equations:
        :return:
        """
        root = list(range(26))

        def find(x: int) -> int:

            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x: int, y: int):
            x, y = find(x), find(y)
            root[x] = y

        for equation in equations:

            if equation[1] == '=':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                union(x, y)

        for equation in equations:

            if equation[1] == '!':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True
