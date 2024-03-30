from typing import List


class Combinations:

    def getCombinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N ^ (T / M + 1))
        S: O(T / M)
        :param candidates:
        :param target:
        :return:
        """
        sumCombinations = []

        def backtrack(pos: int, remaining: int, combo: List[int]):

            if remaining == 0:
                sumCombinations.append(combo[:])
                return
                # base case
            if remaining < 0:
                return  # backtrack

            for nextPos in range(pos, len(candidates)):
                combo.append(candidates[nextPos])
                backtrack(nextPos, remaining - candidates[nextPos], combo)
                combo.pop()

        backtrack(0, target, [])
        return sumCombinations


if __name__ == "__main__":
    combinations = Combinations()
    print(combinations.getCombinationSum([2, 3, 6, 7], 7))
    print(combinations.getCombinationSum([2, 3, 5], 8))
