from typing import List


class Array:

    def sub_array_minimums(self, arr: List[int]) -> int:
        """
        Approach: Monotonically increasing stack
        T: O(N)
        S: O(n)
        :param arr:
        :return:
        """

        stack: List[int] = []
        MOD = 10**9 + 7
        min_sums: int = 0

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                pivot = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                count = (pivot - left) * (right - pivot)
                min_sums += (count * arr[pivot])
            stack.append(i)
        return min_sums % MOD
