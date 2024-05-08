from typing import List


class Permutations:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N * N!)
        S: O(N)
        :param nums:
        :return:
        """

        result = []

        def backtrack(path: List[int]):

            if len(nums) == len(path):
                result.append(list(path))
                return

            for index in range(len(nums)):
                if nums[index] not in path:
                    path.append(nums[index])
                    backtrack(path)
                    path.pop()
        backtrack([])
        return result