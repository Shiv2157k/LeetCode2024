from math import ceil


class BasicCalculatorII:

    def calculate_v0(self, s: str) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        if not s or len(s) == 0:
            return 0

        operator = '+'
        curr_num = 0
        result = 0
        stack = []

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                curr_num = (curr_num * 10) + ord(char) - ord('0')

            if not char.isdigit() and not char.isspace() or i == len(s) - 1:

                if operator in {'+', '-'}:
                    stack.append(curr_num if operator == '+' else -curr_num)
                elif operator == '*':
                    stack.append(stack.pop() * curr_num)
                elif operator == '/':
                    stack.append(ceil(stack.pop() / curr_num))

                operator = char
                curr_num = 0

        while stack:
            result += stack.pop()
        return result

    def calculate_v1(self, s: str) -> int:
        """
        Approach: Without extra space
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        if not s or len(s) == '0':
            return 0

        result = 0
        last_number = 0
        curr_number = 0
        operator = '+'
        n = len(s)

        for i in range(n):
            char = s[i]

            if char.isdigit():
                curr_number = (curr_number * 10) + (ord(char) - ord('0'))

            if not char.isdigit() and char != ' ' or i == n - 1:

                if operator in {'+', '-'}:
                    result += last_number
                    last_number = curr_number if operator == '+' else -curr_number
                elif operator == '*':
                    last_number *= curr_number
                elif operator == '/':
                    last_number = ceil(last_number / curr_number)

                curr_number = 0
                operator = char
        result += last_number
        return result
