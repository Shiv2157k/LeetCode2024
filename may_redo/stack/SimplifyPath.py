from typing import List


class SimplifyPath:

    def simplify_path(self, path: str) -> str:
        """
        Approach: stack
        T: O(N)
        S: O(N)
        :param path:
        :return:
        """

        refined_path: List[str] = path.split('/')
        stack: List[str] = []

        for char in refined_path:

            if char == '..':
                if stack:
                    stack.pop()
            elif char == '.' or not char:
                continue
            else:
                stack.append(char)
        return '/' + '/'.join(stack)
