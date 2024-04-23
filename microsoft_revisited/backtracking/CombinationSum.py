from typing import List


class CombinationSum:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N ^ T/M + 1)
        S: O(T / M)
        :param candidates:
        :param target:
        :return:
        """

        def backtrack(pos: int, remain: int, path: List[int]):

            # base
            if remain == 0:
                # reached target
                output.append(path[:])
                return

            if remain < 0:
                # target exceeded
                return

            for i in (pos, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remain - candidates[i], path)
                path.pop()

        output = []
        backtrack(0, target, [])
        return output
