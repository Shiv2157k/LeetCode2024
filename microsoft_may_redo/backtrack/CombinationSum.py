from typing import List


class CombinationSum:

    def get_combinations(self, candidates: List[int], target: int):
        """
        Approach: Backtracking
        T: O(N ^ (T / M + 1))
        S: O(T / M)
        :param candidates:
        :param target:
        :return:
        """

        def backtrack(pos: int, remain: int, path: List[int]):

            if remain == 0:
                output.append(list(path))
                return
            if remain < 0:
                return

            for i in range(pos, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remain - candidates[i], path)
                path.pop()

        output = []
        backtrack(0, target, [])
        return output
