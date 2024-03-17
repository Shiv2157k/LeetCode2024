

class Parantheses:
    def is_valid(self, s: str) -> bool:
        """
        Approach: Using Stack
        Time Complexity: O(N) -> need to iterate over all the characters
        Space Complexity: O(N) -> edge case with non valid we need to store everything in stack.
        :param s:
        :return:
        """
        # to track the valid parantheses
        stack = []
        # to store the valid closing brackets
        parantheses_map = {"}": "{", "]": "[", ")": "("}

        # iterate over each character in the string
        for char in s:
            # if closed brackets are found
            # time to pop and verify valid or not
            if char in parantheses_map:
                top_element = stack.pop() if stack else "$"
                # verify whether the top element
                # is matching with the current char
                if top_element != parantheses_map[char]:
                    return False
            else: # push all the open brackets to stack
                stack.append(char)
        # if the stack is empty it is true not empty then false
        return not stack


if __name__ == "__main__":
    parantheses = Parantheses()
    print(parantheses.is_valid("(())(({}))[]"))
    print(parantheses.is_valid("{}[]()"))
    print(parantheses.is_valid("()"))
    print(parantheses.is_valid("(["))
    print(parantheses.is_valid("{"))
    print(parantheses.is_valid("(())((())){{}][]"))