class BasicCalculatorII:

    def calculateV1(self, s: str) -> int:

        if not s or len(s) == 0:
            return 0

        n = len(s)
        currentNumber = 0
        lastNumber = 0
        operation = '+'
        result = 0

        for i in range(n):

            char = s[i]

            if char.isdigit():
                currentNumber = (currentNumber * 10) + (ord(char) - ord('0'))

            if not char.isdigit() and char != ' ' or i == n - 1:

                if operation in {'+', '-'}:
                    result += lastNumber
                    lastNumber = -currentNumber if operation == '-' else currentNumber
                elif char == '*':
                    lastNumber *= currentNumber
                elif char == '/':
                    lastNumber = int(lastNumber / currentNumber)
                operation = char
                currentNumber = 0
        result += lastNumber
        return result

    def calculateV0(self, s: str) -> int:

        if not s or len(s) == 0:
            return 0

        n = len(s)
        stack = []
        currentNumber = 0
        operation = '+'

        for i in range(n):
            char = s[i]

            if char.isdigit():
                currentNumber = currentNumber * 10 + ord(char) - ord('0')

            if not char.isdigit() and not char.isspace() or i == n - 1:

                if operation == '-':
                    stack.append(-currentNumber)
                elif operation == '+':
                    stack.append(currentNumber)
                elif operation == '*':
                    stack.append(stack.pop() * currentNumber)
                elif operation == '/':
                    stack.append(int(stack.pop() / currentNumber))
                operation = char
                currentNumber = 0
        result = 0
        while stack:
            result += stack.pop()
        return result
