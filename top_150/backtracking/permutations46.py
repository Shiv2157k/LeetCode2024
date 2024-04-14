from typing import List


class Permutation:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back Track
        T: O(N * N!)
        S: O(N)
        :param nums:
        :return:
        """
        result = []

        def backtrack(path: List[int]) -> None:

            if len(nums) == len(path):
                result.append(path[:])
                return

            for index in range(len(nums)):
                if nums[index] not in path:
                    path.append(nums[index])
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result


if __name__ == "__main__":
    permutation = Permutation()
    print(permutation.permute([1, 2, 3]))
    print(permutation.permute([1]))
    print(permutation.permute([1, 2]))
