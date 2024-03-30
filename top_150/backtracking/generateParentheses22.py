from collections import deque
from typing import List


class Parentheses:

    def generateValidCombinationsV0(self, n: int) -> List[str]:
        """
        Approach: BruteForce / Queue (BFS)
        T: O(2^n * n)
        S: O(2^n * n)
        :param n:
        :return:
        """
        validParentheses = []

        def isValid(path: List[str]):
            leftCount = 0

            for char in path:
                if char == "(":
                    leftCount += 1
                else:
                    leftCount -= 1
                if leftCount < 0:
                    return False
            return leftCount == 0

        queue = deque([""])

        while queue:
            curr = queue.popleft()

            if len(curr) == 2 * n:
                if isValid(curr):
                    validParentheses.append(curr)
                continue
            queue.append(curr + "(")
            queue.append(curr + ")")
        return validParentheses

    def generateValidCombinationsV1(self, n: int) -> List[str]:
        """
        Approach: Back Tracking
        T: O(4^n / sqrt(n))
        S: O(n)
        :param n:
        :return:
        """
        validParentheses = []

        def backtrack(leftCount: int, rightCount: int, path: List[str]):

            if len(path) == 2 * n:
                validParentheses.append("".join(path))
                return

            if leftCount < n:
                path.append("(")
                backtrack(leftCount + 1, rightCount, path)
                path.pop()

            if leftCount > rightCount:
                path.append(")")
                backtrack(leftCount, rightCount + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return validParentheses


if __name__ == "__main__":

    parentheses = Parentheses()
    print(parentheses.generateValidCombinationsV1(3))
    print(parentheses.generateValidCombinationsV0(3))

    print(parentheses.generateValidCombinationsV1(2))
    print(parentheses.generateValidCombinationsV0(2))