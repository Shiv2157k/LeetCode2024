from typing import List


class Parentheses:

    def generate(self, n: int) -> List[str]:
        """
        Approach: BackTrack
        T: O(4^n / sqrt(n))
        S: O(n)
        :param n:
        :return:
        """

        def backtrack(left: int, right: int, path: List[str]):

            if len(path) == n * 2:
                output.append("".join(path))
                return

            if left < n:
                path.append(')')
                backtrack(left + 1, right, path)
                path.pop()

            if left > right:
                path.append('(')
                backtrack(left, right + 1, path)
                path.pop()

        output = []
        backtrack(0, 0, [])
        return output
