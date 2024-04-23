from typing import List, Any


class BasicCalculator:  # 224

    def calculate(self, s: str) -> int:

        stack: List[Any] = []
        operator = '+'
        curr_num = 0
        # for convenience
        s += '@'

        n = len(s)
        sign: int = 1

        for i in range(n):

            char = s[i]

            if char.isdigit():
                curr_num = curr_num * 10 + (ord(char) - ord('0'))
            elif char == '(':
                stack.append(operator)
                operator = '+'
            elif not char.isspace():

                if i == 1 and operator == '-' and sign == 1:
                    sign = -1

                if operator in {'*', '/'}:
                    stack.append(self._evaluate(operator, stack.pop(), curr_num))
                else:
                    stack.append(self._evaluate(operator, curr_num))

                operator = char
                curr_num = 0

                if char == ')':
                    while stack[-1] not in {'/', '-', '*', '+'}:
                        curr_num += stack.pop()
                    operator = stack.pop()

        result = 0
        while stack:
            result += stack.pop()

        return result * sign

    def _evaluate(self, operator: str, x: int, y: int = 0) -> int:
        output = x
        if operator == '-':
            output = -output
        elif operator == '*':
            output *= y
        elif operator == '/':
            output = int(x / y)
        return output
