from typing import List


class SubsetsII:


    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtrack
        T: O()
        S: O()
        :param nums:
        :return:
        """

        nums.sort()

        def backtrack(pos: int, path: List[int]):

            subsets.append(list(path))

            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        subsets = []
        backtrack(0, [])
        return subsets