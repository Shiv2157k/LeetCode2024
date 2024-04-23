class Parentheses:

    def isValid(self, s: str) -> bool:
        """
        Approach: Stack and Map
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        stack = []
        parenthesesMap = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in parenthesesMap:
                topElement = stack.pop() if stack else '#'
                if topElement != parenthesesMap[char]:
                    return False
            else:
                stack.append(char)
        return not stack  # len(stack) == 0
