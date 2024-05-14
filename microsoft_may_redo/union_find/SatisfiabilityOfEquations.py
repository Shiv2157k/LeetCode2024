from typing import List


class SatisfiabilityOfEquations:

    def equation_possible(self, equations: List[str]) -> bool:
        """
        Approach: Union Find
        T: O(N)
        S: O(N)
        :param equations:
        :return:
        """
        # root = [0, 1, 2, 3....25]
        root = list(range(26))

        def find(x: int) -> int:
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x: int, y: int):
            x, y = find(x), find(y)
            root[x] = y

        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)

        for eq in equations:
            if eq[0] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True
