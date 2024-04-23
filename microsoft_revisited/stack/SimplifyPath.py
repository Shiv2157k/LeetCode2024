class SimplifyPath:

    def simplifyPath(self, path: str) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param path:
        :return:
        """
        input = path.split('/')

        stack = []

        for char in input:

            if char == '..':
                if stack:
                    stack.pop()
            elif char == '.' or not char:
                continue
            else:
                stack.append(char)
        return '/' + '/'.join(stack)
