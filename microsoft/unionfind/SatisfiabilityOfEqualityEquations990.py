from typing import List


class Equations:

    def equationsSatisfy(self, equations: List[str]) -> bool:
        """
        Approach: Union Find
        T: O(Nlog∣Σ∣)
        S: O(∣Σ∣) -> O(1)
        :param equations:
        :return:
        """

        root = list(range(26))

        def find(x: int):
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
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True
