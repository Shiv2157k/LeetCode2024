class ValidParenthesisString:

    def checkValidString(self, s: str) -> bool:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param s: 
        :return: 
        """
        openCount = 0
        closeCount = 0

        length = len(s) - 1

        for i in range(length + 1):

            if s[i] == '(' or s[i] == '*':
                openCount += 1
            else:
                openCount -= 1

            if s[length - i] == ')' or s[length - i] == '*':
                closeCount += 1
            else:
                closeCount -= 1

            if openCount < 0 or closeCount < 0:
                return False
        return True