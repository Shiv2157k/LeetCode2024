class RemoveKDigits:

    def remove_k_large_digits(self, num: str, k: int) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param num:
        :param k:
        :return:
        """

        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        for _ in range(k):
            stack.pop()

        is_leading_zero = True
        result = []

        for num in stack:
            if is_leading_zero and num == '0':
                continue
            is_leading_zero = False
            result.append(num)
        return '0' if len(result) == '0' else ''.join(result)
