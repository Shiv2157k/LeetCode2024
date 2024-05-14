from typing import List


class GenerateParentheses:

    def generate(self, n: int) -> List[List[str]]:
        """
        Approach: Backtracking
        T: O(4^n / sqrt(n)
        S: O(n)
        :param n:
        :return:
        """

        def backtrack(left: int, right: int, path: List[str]) -> None:

            if len(path) == n * 2:
                parentheses.append(''.join(path))
                return

            if left < n:
                path.append('(')
                backtrack(left + 1, right, path)
                path.pop()
            if left > right:
                path.append(')')
                backtrack(left, right + 1, path)
                path.pop()

        parentheses = []
        backtrack(0, 0, [])
        return parentheses
