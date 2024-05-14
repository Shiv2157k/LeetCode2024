from typing import List


class SubArrayMinimums:

    def sum_of_minimums(self, arr: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param arr:
        :return:
        """

        MOD = 10 ** 9 + 7
        stack = []
        sum_of_min = 0

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                count = (mid - left) * (right - mid)
                sum_of_min += (count * arr[mid])
            stack.append(i)
        return sum_of_min % MOD
