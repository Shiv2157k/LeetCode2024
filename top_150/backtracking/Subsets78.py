from typing import List


class SubSets:

    def generateV1(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back Tracking
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """

        result = []

        def backtrack(pos: int, path: List[int]) -> None:
            result.append(path[:])
            for nextPos in range(pos, len(nums)):
                path.append(nums[nextPos])
                backtrack(nextPos + 1, path)
                path.pop()

        backtrack(0, [])
        return result

    def generateV0(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back Track
        T: O(N * 2^N)
        S: O(N)
        :param nums:
        :return:
        """

        result = []

        def backtrack(pos: int=0, path: List[int]=[]):

            if len(path) == k:
                result.append(path[:])
                return

            for nextPos in range(pos, len(nums)):
                path.append(nums[nextPos])
                backtrack(nextPos + 1, path)
                path.pop()

        for k in range(len(nums) + 1):
            backtrack()
        return result


if __name__ == "__main__":

    subSets = SubSets()
    print(subSets.generateV0([1, 2, 3]))
    print(subSets.generateV1([1, 2, 3]))
