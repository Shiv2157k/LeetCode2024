from typing import List


class Subsets:

    def generateV0(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """

        def backtrack(pos: int, path: List[int]):

            output.append(list(path))

            for nextPos in range(pos, len(nums)):
                path.append(nums[nextPos])
                backtrack(nextPos + 1, path)
                path.pop()

        output = []
        backtrack(0, [])
        return output

    def generateV1(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """

        def backtrack(pos: int, path: List[int]):

            if len(path) == k:
                result.append(list(path))
                return

            for i in range(pos, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
        return result
