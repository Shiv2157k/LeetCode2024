from typing import List


class SubsetsII:

    def subset_with_dup(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """
        nums.sort()

        def backtrack(pos: int, path: List[int]):

            subsets.append(list(path))

            for next_pos in range(pos, path):

                if next_pos > pos and nums[next_pos] == nums[next_pos - 1]:
                    continue
                path.append(nums[next_pos])
                backtrack(next_pos + 1, path)
                path.pop()

        subsets = []
        backtrack(0, [])
        return subsets
