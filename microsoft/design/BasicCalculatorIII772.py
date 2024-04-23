class BasicCalculatorIII:

    def calculate(self, s: str) -> int:

        stack = []
        currNum = 0
        operator = '+'
        # for convenience
        s += '@'

        for i in range(len(s)):
            char = s[i]

            # check for digit
            if char.isdigit():
                currNum = (currNum * 10) + (ord(char) - ord('0'))
            # open bracket encountered push operator to stack and reset operator to '+'
            elif char == '(':
                stack.append(operator)
                operator = '+'
            else:  # otherwise
                # perform below
                if operator in {'*', '/'}:
                    stack.append(self.evaluate(operator, stack.pop(), currNum))
                # set -currNum operator is '-
                else:
                    stack.append(self.evaluate(operator, currNum))
                # reset the currNum and assign new operator
                currNum = 0
                operator = char
                # encountered ending bracket
                if char == ')':
                    # until we don't see an operator re-build currNum by pop and add
                    while stack[-1] not in {'/', '*', '+', '-'}:
                        currNum += stack.pop()
                    # reset the operator
                    operator = stack.pop()
        result = 0
        while stack:
            result += stack.pop()
        return result

    def evaluate(self, operator: str, x: int, y: int = 0) -> int:
        if operator == '-':
            return -x
        elif operator == '*':
            return x * y
        elif operator == '/':
            return int(x / y)
        return x
