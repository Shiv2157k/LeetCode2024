from typing import List


class Combinations:

    def generate_v1(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        def backtrack(pos: int, path: List[int]):

            if len(path) == k:
                combinations.append(path[:])
                return

            need = k - len(path)
            remain = n - pos + 1
            available = remain - need

            for num in range(pos, pos + available + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return combinations

    def generate_v0(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Backtracking
        T: O(n! / k! (n - k)!)
        S: O(k)
        :param n:
        :param k:
        :return:
        """

        def backtrack(pos: int, path: List[int]) -> None:

            if len(path) == k:
                combinations.append(path[:])
                return

            for num in range(pos, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        combinations = []
        backtrack(1, [])
        return combinations
