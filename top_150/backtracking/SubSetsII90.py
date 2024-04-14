from typing import List


class SubSetII:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking
        T: O(N * 2 ^ N)
        S: O(N)
        :param nums:
        :return:
        """
        nums.sort()
        result = []

        def backtrack(path: List[int], pos: int) -> None:

            result.append(path[:])

            for nextPos in range(pos, len(nums)):
                if nextPos > pos and nums[nextPos] == nums[nextPos - 1]:
                    continue
                path.append(nums[nextPos])
                backtrack(path, nextPos + 1)
                path.pop()

        backtrack([], 0)
        return result


if __name__ == "__main__":
    subset = SubSetII()
    print(subset.subsetsWithDup([1, 2, 2]))
