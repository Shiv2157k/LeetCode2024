from typing import List


class Combinations:

    def find_combinations_III(self, k: int, n: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        T:
        S:

        :param k:
        :param n:
        :return:
        """
        results = []
        def backtrack(remain: int, combinations: List[int], pointer: int):
            """

            :param remain:
            :param combinations:
            :param pointer:
            :return:
            """
            # base case
            if remain == 0 and len(combinations) == k:
                results.append(list(combinations))
                return
            elif remain < 0 or len(combinations) == k:
                return

            for i in range(pointer, 9):
                combinations.append(i + 1)
                backtrack(remain - i - 1, combinations, i + 1)
                combinations.pop()
        backtrack(n, [], 0)
        return results

    def find(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        T: O(N ^ T/M + 1) -> Height of the DFS
        S: O(T/ M)
        :param candidates:
        :param target:
        :return:
        """
        results = []
        def backtracking(remaining, combinations, start):
            # base cases
            if remaining == 0:  # reached target
                # deep copy of valid combination
                results.append(list(combinations))
                # end of back track
                return
            elif remaining < 0: # way more than target sum
                # end of back track
                return
            # logic for all the combination generation
            for i in range(start, len(candidates)):
                # add it to the combination list
                combinations.append(candidates[i])
                # back track
                backtracking(remaining - candidates[i], combinations, i)
                # pop the combination
                # it is either added or not reached the target
                # start with next candidate
                combinations.pop()
        backtracking(target, [], 0)
        return results


if __name__ == "__main__":
    combinations = Combinations()
    # print(combinations.find([2, 3, 6, 7], 7))
    # print(combinations.find([3, 4, 5], 8))
    print(combinations.find_combinations_III(3, 7))
    print(combinations.find_combinations_III(2, 9))