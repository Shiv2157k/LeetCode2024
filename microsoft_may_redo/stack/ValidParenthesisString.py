class ValidParenthesisString:

    def is_valid(self, s: str) -> bool:
        """
        Approach: STack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        open_stack = []
        asterisk_stack = []

        for i, char in enumerate(s):

            if char == '(':
                open_stack.append(i)
            elif char == '*':
                asterisk_stack.append(i)
            else:

                if open_stack:
                    open_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False

        while open_stack and asterisk_stack:
            if open_stack.pop() > asterisk_stack.pop():
                return False
        return not open_stack
