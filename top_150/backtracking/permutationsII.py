from typing import List, Dict


class PermutationII:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: BackTrack
        T: O(N! / (N - k)!)
        S: O(N) + O(N) .. -> O(N)
        :param nums:
        :return:
        """
        results = []

        def backtrack(path: List[int], freq: Dict):

            if len(nums) == len(path):
                results.append(list(path))

            for num in freq:
                if freq[num] > 0:
                    freq[num] -= 1
                    path.append(num)
                    backtrack(path, freq)
                    freq[num] += 1
                    path.pop()

        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        backtrack([], numFreq)
        return results


if __name__ == "__main__":
    perm = PermutationII()
    print(perm.permuteUnique([1, 1, 2]))
    print(perm.permuteUnique([1, 2, 3]))
