class FilePath:

    def simplifyPath(self, path: str) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param path:
        :return:
        """
        stack = []
        # split by "/" and traverse
        for component in path.split("/"):
            # if double period is encountered and
            # there is value in stack go up one level by stack pop
            if component == "..":
                if stack:
                    stack.pop()
            # if it's a simple period or empty string just ignore
            elif component == "." or not component:
                continue
            # otherwise add it into stack
            else:
                stack.append(component)
        # root is "/" add that first before joining
        return "/" + "/".join(stack)


if __name__ == "__main__":
    filePath = FilePath()
    print(filePath.simplifyPath("/a/b//c/.././d/../f"))
    print(filePath.simplifyPath("/../"))
