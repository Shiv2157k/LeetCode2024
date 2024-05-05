from typing import List


class Subsets:

    def generate(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N * 2^N)
        S: O(N) - without subsets into consideration else O(N * 2^N)
        :param nums:
        :return:
        """

        def backtrack(pos: int, path: List[int]) -> None:
            subsets.append(list(path))

            for next_pos in range(pos, len(nums)):
                path.append(nums[next_pos])
                backtrack(next_pos + 1, path)
                path.pop()

        subsets = []
        backtrack(0, [])
        return subsets
