from typing import List


class PermutationsII:

    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N * N!)
        S: O(N)
        :param nums:
        :return:
        """

        freq_checker = {}
        for num in nums:
            freq_checker[num] = freq_checker.get(num, 0) + 1

        def backtrack(path: List[int]):

            if len(nums) == len(path):
                result.append(path[:])
                return

            for num in freq_checker:
                if freq_checker[num] > 0:
                    path.append(num)
                    freq_checker[num] -= 1
                    backtrack(path)
                    path.pop()
                    freq_checker[num] += 1

        result = []
        backtrack([])
        return result
