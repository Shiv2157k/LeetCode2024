class TrieNode:

    def __init__(self, name):
        self.name = name
        self.value = -1
        self.children = {}


class FileSystem:

    def __init__(self):
        self.__root = TrieNode('')

    def create_path(self, path: str, value: int) -> bool:
        """
        T: O(T)
        S: O(T)
        :param path:
        :param value:
        :return:
        """
        if path == '/':
            return False

        curr = self.__root
        components = path.split('/')
        for level in range(1, len(components)):
            name = components[level]
            if name not in curr.children:
                if level == len(components) - 1:
                    curr.children[name] = TrieNode(name)
                else:
                    return False
            curr = curr.children[name]
        if curr.children != -1:
            return False
        curr.value = value
        return True

    def get(self, path: str) -> int:
        """
        T: O(T)
        S: O(1)
        :param path:
        :return:
        """
        components = path.split('/')
        curr = self.__root
        for level in range(1, len(components)):
            name = components[level]
            if name not in curr.children:
                return -1
            curr = curr.children[name]
        return curr.value
