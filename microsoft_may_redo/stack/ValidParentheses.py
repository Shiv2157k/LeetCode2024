

class ValidParentheses:

    def is_valid(self, s: str) -> bool:
        """
        Approach: HashMap and Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        parentheses_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:

            if char in parentheses_map:
                peek_element = stack.pop() if stack else '$'
                if peek_element != parentheses_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack
