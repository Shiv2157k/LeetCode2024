from typing import List


class SumOfSubarrayMinimums:


    def sumSubarrayMin(self, arr: List[int]) -> int:
        """
        Approach: Monotonic Stack
        T: O(N)
        S: O(N)
        :param arr:
        :return:
        """

        MOD = 10**9 + 7
        # monotonic stack to store the indices
        # for calculating left and right boundaries
        stack = []
        sumOfMin = 0

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                sumOfMin += (count * arr[mid])
            stack.append(i)
        return sumOfMin % MOD