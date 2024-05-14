from typing import List


class PermutationsII:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: BackTrack
        T: O(E(n, k=1) P(N, K))
        S: O(N)
        :param nums:
        :return:
        """

        def backtrack(path: List[int]) -> None:

            if len(nums) == len(path):
                permutations.append(list(path))
                return

            for num in num_freq.keys():
                if num_freq[num] > 0:
                    path.append(num)
                    num_freq[num] -= 1
                    backtrack(path)
                    num_freq[num] += 1
                    path.pop()


        permutations = []
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        backtrack([])
        return permutations
