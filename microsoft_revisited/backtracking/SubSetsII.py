from typing import List


class SubSetsII:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back Track
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """
        nums.sort()

        def backtrack(pos: int, path: List[int]):

            output.append(list(path))

            for i in range(pos, len(nums)):

                if i > pos and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        output = []
        backtrack(0, [])
        return output
