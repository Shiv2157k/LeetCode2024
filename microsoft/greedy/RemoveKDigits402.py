class RemoveKDigits:

    def remove(self, num: str, k: int):

        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        for _ in range(k):
            stack.pop()

        isLeadingZero = True
        result = []
        for digit in stack:
            if isLeadingZero and digit == '0':
                continue
            isLeadingZero = False
            result.append(digit)

        return '0' if len(result) == 0 else ''.join(result)
