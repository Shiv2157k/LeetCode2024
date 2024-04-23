from typing import List


class RemoveKDigits:

    def remove_k_digits(self, num: str, k: int) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param num:
        :param k:
        :return:
        """

        stack: List[str] = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)
        
        for _ in range(k):
            stack.pop()

        is_leading_zero: bool = True
        result = []

        for digit in stack:
            if is_leading_zero and digit == '0':
                continue
            is_leading_zero = False
            result.append(digit)
        return '0' if len(result) == 0 else ''.join(result)