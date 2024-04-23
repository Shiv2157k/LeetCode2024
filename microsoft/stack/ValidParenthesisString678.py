class ValidParenthesisString:

    def checkValidString(self, s: str) -> bool:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s: 
        :return: 
        """
        
        openBracketStack = []
        asterickStack = []

        for i, char in enumerate(s):

            if char == '(':
                openBracketStack.append(i)
            elif char == '*':
                openBracketStack.append(i)
            else:

                if openBracketStack:
                    openBracketStack.pop()
                elif asterickStack:
                    asterickStack.pop()
                else:
                    return False

        while openBracketStack and asterickStack:
            if openBracketStack.pop() > asterickStack.pop():
                return False
        return not openBracketStack
