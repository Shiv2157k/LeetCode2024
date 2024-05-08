from typing import List


class CombinationSumII:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(2^N)
        S: O(N)
        :param candidates:
        :param target:
        :return:
        """
        # make sure the sort the candidates for handling duplicates
        candidates.sort()

        def backtrack(pos: int, remain: int, path: List[int]):

            if remain == 0:
                output.append(list(path))
                return
            if remain < 0:
                return

            for next_pos in range(pos, len(candidates)):
                if next_pos > pos and candidates[next_pos] == candidates[next_pos - 1]:
                    continue
                path.append(candidates[next_pos])
                backtrack(next_pos + 1, remain - candidates[next_pos], path)
                path.pop()

        output = []
        backtrack(0, target, [])
        return output
