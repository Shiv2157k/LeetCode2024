class Parentheses:

    def isValid(self, s: str) -> bool:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        stack = []
        parenthesesMap = {"}": "{", ")": "(", "]": "["}

        for char in s:

            if char in parenthesesMap:
                topChar = stack.pop() if stack else "$"
                if topChar != parenthesesMap[char]:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.isValid("()[]{}"))
    print(parentheses.isValid("()[[]{}"))
