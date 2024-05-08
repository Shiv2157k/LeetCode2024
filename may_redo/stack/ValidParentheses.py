from typing import List, Dict


class Parentheses:


    def is_valid(self, s: str) -> bool:
        """
        Approach: Stack and HashMap
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        if not s:
            return True

        stack: List[str] = []
        parentheses_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            if char in parentheses_map:
                top_element = stack.pop() if stack else '$'
                if top_element != parentheses_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack