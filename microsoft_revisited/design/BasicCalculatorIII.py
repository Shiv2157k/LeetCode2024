from typing import List, Any


class BasicCalculatorIII:

    def calculate(self, s: str) -> int:
        """
        Approach: As per book
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        stack: List[Any] = []
        curr_num: int = 0
        operator: str = '+'
        # for convenience
        s += '@'

        for char in s:

            if char.isdigit():
                curr_num = (curr_num * 10) + (ord(char) - ord('0'))
            elif char == '(':
                stack.append(operator)
                operator = '+'
            else:

                if operator in {'*', '/'}:
                    stack.append(self._evaluate(operator, stack.pop(), curr_num))
                else:
                    stack.append(self._evaluate(operator, curr_num, 0))

                operator = char
                curr_num = 0

                if char == ')':
                    while stack[-1] not in {'+', '-', '*', '/'}:
                        curr_num += stack.pop()
                    operator = stack.pop()

        result: int = 0
        while stack:
            result += stack.pop()
        return result

    def _evaluate(self, operator: str, x: int, y: int = 0):

        output = x
        if operator == '-':
            output *= -1
        elif operator == '*':
            output *= y
        elif operator == '/':
            output = int(x / y)
        return output
