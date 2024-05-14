class BasicCalculatorIII:

    def calculate(self, s: str) -> int:
        """
        Approach:
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        # sentinel for convenience
        s += '@'
        operator = '+'
        current_number = 0
        stack = []

        for char in s:

            if char.isdigit():
                current_number = (current_number * 10) + (ord(char) - ord('0'))
            elif char == '(':
                # append operator and result to default
                stack.append(operator)
                operator = '+'
            else:

                if operator in {'*', '+'}:
                    stack.append(self.__evaluate(operator, stack.pop(), current_number))
                else:
                    stack.append(self.__evaluate(operator, current_number, 0))

                current_number = 0
                operator = char

                if char == ')':
                    while stack[-1] not in {'*', '/', '+', '-'}:
                        current_number += stack.pop()
                    operator = stack.pop()

        result = 0
        while stack:
            result += stack.pop()
        return result

    def __evaluate(self, operator: str, x: int, y: int = 0):
        result = x
        if operator == '-':
            result *= -1
        elif operator == '*':
            result = x * y
        elif operator == '/':
            result = int(x / y)
        return result
