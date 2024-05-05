from typing import List


class ValidParenthesis:

    def check_valid_string_v0(self, s: str) -> bool:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s: 
        :return: 
        """

        open_brackets_stack: List[int] = []
        aestrick_stack: List[int] = []

        for i, char in enumerate(s):

            if char == '(':
                open_brackets_stack.append(i)
            elif char == '*':
                open_brackets_stack.append(i)
            else:
                if open_brackets_stack:
                    open_brackets_stack.pop()
                elif aestrick_stack:
                    aestrick_stack.pop()
                else:
                    return False

        while open_brackets_stack and aestrick_stack:
            if open_brackets_stack.pop() > aestrick_stack.pop():
                return False
        return not open_brackets_stack

    def check_valid_string_v1(self, s: str) -> bool:
        """
        Approach: Linear with no extra space
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        open_count: int = 0
        close_count: int = 0
        length: int = len(s) - 1

        for i in range(length + 1):

            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1

            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1

            if open_count < 0 or close_count < 0:
                return False
        return True
