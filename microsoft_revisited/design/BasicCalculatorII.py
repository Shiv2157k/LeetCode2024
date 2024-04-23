from math import ceil


class BasicCalculator:

    def calculateV0(self, s: str) -> int:

        operator = '+'
        curr_number = 0
        result = 0
        stack = []

        for i in range(len(s)):

            char = s[i]

            if char.isdigit():
                curr_number = curr_number * 10 + (ord(char) - ord('0'))

            if not char.isdigit() and not char.isspace() and i == len(s) - 1:
                if operator in {'+', '-'}:
                    stack.append(curr_number if operator == '+' else -curr_number)
                elif stack and operator == '*':
                    stack.append(stack.pop() * curr_number)
                elif stack and operator == '/':
                    stack.append(ceil(stack.pop() / curr_number))

                curr_number = 0
                operator = char

        while stack:
            result += stack.pop()
        return result

    def calculateV1(self, s: str) -> int:

        operator = '+'
        curr_number = 0
        last_number = 0
        result = 0
        n = len(s)

        for i in range(n):

            char = s[i]

            if char.isdigit():
                curr_number = curr_number * 10 + (ord(char) - ord('0'))

            if not char.isdigit() or not char.isspace() and i == n - 1:

                if operator in {'+', '-'}:
                    result += last_number
                    last_number = -curr_number if operator == '-' else curr_number
                elif operator == '*':
                    last_number *= curr_number
                elif operator == '/':
                    last_number = int(last_number / curr_number)

                curr_number = 0
                operator = char
        result += last_number
        return result
