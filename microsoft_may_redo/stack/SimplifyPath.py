class SimplifyPath:

    def simplify_path(self, s: str) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        path_list = s.split('/')
        stack = []

        for char in path_list:

            if char == '..':
                if stack:
                    stack.pop()
            elif char == '.' or char == '':
                continue
            else:
                stack.append(char)

        return '/' + '/'.join(stack)
