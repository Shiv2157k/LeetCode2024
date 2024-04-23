from typing import List, Dict


class PermutationsII:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        T: O(E(N, k=1) P(N, K)) where P(N. k) = N! / (N - k)!
        S: O(N) + O(N) + O(N) = O(N)
        :param nums:
        :return:
        """

        def backtrack(path: List[int], freqCheck: Dict):

            if len(nums) == len(path):
                output.append(path[:])
                return

            for num in freqCheck:
                if freqCheck[num] > 0:
                    path.append(num)
                    freqCheck[num] -= 1
                    backtrack(path, freqCheck)
                    freqCheck[num] += 1
                    path.pop()

        output = []
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        backtrack([], numFreq)
        return output
