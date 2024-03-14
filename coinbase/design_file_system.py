from collections import defaultdict


class TrieNode:

    def __init__(self, name: int):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1


class FileSystem:

    def __init__(self):
        self.root = TrieNode("", 0)

    def create_path(self, path: str, value: int):

        components = path.split("/")
        curr = self.root

        for i in range(1, len(components)):
            name = components[i]
            if name not in curr[map]:
                # if component is the last then we add it to the map
                if name == components[-1]:
                    curr.map[name] = TrieNode(name)
                else:
                    return False
            curr = curr[name].map
        if curr.value != -1:
            return False
        curr.value = value
        return True

    def get(self, path: str) -> int:
        components = path.split("/")
        curr = self.root

        for i in range(1, len(components)):
            name = components[i]
            if name not in curr[map]:
                return -1
            curr = curr[name].map
        return curr.value


class FileSystem_v0:

    def __init__(self):
        # root node contains empty string
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:

        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        parent = path[:path.rfind("/")]
        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:

        return self.paths.get(path, -1)
