from typing import Dict, Set, List


class DuplicateLetters:

    def remove(self, s: str) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        stack: List[str] = []
        seen: Set[str] = set()
        last_occurrence: Dict[str, int] = {}

        # build the last occurrence mapping of each char
        for ptr, char in enumerate(s):
            last_occurrence[char] = ptr

        for ptr, char in enumerate(s):

            if char not in seen:

                while stack and stack[-1] > char and last_occurrence[stack[-1]] > ptr:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)
