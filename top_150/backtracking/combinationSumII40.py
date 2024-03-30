from typing import List


class CombinationII:

    def getCombinationSums(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: BackTracking
        T: O(2^N)
        S: O(N)
        :param candidates:
        :param target:
        :return:
        """
        candidates.sort()
        result = []

        def backtrack(pos: int, remain: int, path: List[int]):

            if remain == 0:
                result.append(path[:])
                return
            if remain < 0:
                return

            for nextPos in range(pos, len(candidates)):

                if nextPos > pos and candidates[nextPos] == candidates[nextPos - 1]:
                    continue
                path.append(candidates[nextPos])
                backtrack(nextPos + 1, remain - candidates[nextPos], path)
                path.pop()

        backtrack(0, target, [])
        return result


if __name__ == "__main__":
    combos = CombinationII()
    print(combos.getCombinationSums([10, 1, 2, 7, 6, 1, 5], 8))
    print(combos.getCombinationSums([2, 5, 2, 1, 2], 5))
