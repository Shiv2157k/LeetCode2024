class ValidParenthesisString:

    def check_valid_string(self, s: str) -> bool:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        length = len(s) - 1
        open_bracket_count = 0
        close_bracket_count = 0

        for i in range(length + 1):

            if s[i] == '(' or s[i] == '*':
                open_bracket_count += 1
            else:
                open_bracket_count -= 1

            if s[length - i] == ')' or s[length - i] == '*':
                close_bracket_count += 1
            else:
                close_bracket_count -= 1

            if open_bracket_count < 0 or close_bracket_count < 0:
                return False
        return True
