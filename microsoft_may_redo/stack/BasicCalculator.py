from math import ceil


class BasicCalculator:

    def calculate(self, s: str) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        current_number = 0
        operator = '+'
        stack = []
        sign = 1

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                current_number = (current_number * 10) + (ord(char) - ord('0'))
            elif char == '(':
                # add operator and reset to default i..e, +
                stack.append(operator)
                operator = '+'
            elif not char.isspace():
                if i == 1 and operator == '-' and sign:
                    sign *= -1
                if operator in {'*', '/'}:
                    stack.append(self.__evaluate(operator, stack.pop(), current_number))
                else:
                    stack.append(self.__evaluate(operator, current_number, 0))

                operator = char
                current_number = 0

                if char == ')':
                    while stack[-1] not in {'+', '-', '/', '*'}:
                        current_number += stack.pop()
                    operator = stack.pop()
        result = 0
        while stack:
            result += stack.pop()
        return sign * result

    def __evaluate(self, operator: str, x: int, y: int = 0):
        result = x
        if operator == '-':
            result *= -1
        elif operator == '*':
            result = x * y
        elif operator == '/':
            result = ceil(x / y)
        return result
