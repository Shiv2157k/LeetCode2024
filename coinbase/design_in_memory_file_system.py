from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self, name: str = ""):
        self.child = defaultdict(TrieNode)
        self.is_file = False
        self.name = name
        self.content = ""


class FileSystem:
    """
    Hash Map / Dictionary Based File System
    """

    def __init__(self):
        self.structure = {'/': dict()}

    def ls(self, path: str) -> List[str]:
        destination = self.structure['/']
        for d in path.split('/'):
            if not d:
                continue
            destination = destination[d]

        if isinstance(destination, str):
            return [d]
        return sorted(destination.keys())

    def mkdir(self, path: str) -> None:
        directory = self.structure['/']
        for d in path.split('/'):
            if not d:
                continue
            if not d in directory:
                directory[d] = dict()
            directory = directory[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        directory = self.structure['/']
        path = filePath.split('/')
        file_name = path[-1]
        for d in path[:-1]:
            if not d:
                continue
            directory = directory[d]
        directory[file_name] = directory.get(file_name, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        result = self.structure['/']
        for d in filePath.split('/'):
            if not d:
                continue
            result = result[d]
        return result


class InMemoryFileSystem:

    """
        Time Complexity:

        ls method: O(k log m),
        where k is the length of the input path and m is the total number of nodes in the trie.
        This is because we traverse the trie up to the specified path, and at each level,
        we may need to sort the children, resulting in log m complexity.
        mkdir method: O(k log m),
        where k is the length of the input path and m is the total number of nodes in the trie.
        Similar to ls, we traverse the trie and may need to sort the children.
        addContentToFile method: O(k + n),
        where k is the length of the input file path and n is the length of the content.
        We traverse the trie to the specified path (O(k)), and then append the content (O(n)).
        readContentFromFile method: O(k),
        where k is the length of the input file path.
        We traverse the trie to the specified path.
        Space Complexity:
        O(m + n), where m is the total number of nodes in the trie,
        and n is the total content size in the trie.
        The trie structure itself contributes to the space complexity, and the content size adds to it.
    """

    def __init__(self):
        self.root = TrieNode()

    def traverse(self, file_path: str) -> TrieNode:
        curr = self.root
        components = file_path.split("/")
        for index in range(1, len(components)):
            component = components[index]
            curr = curr.child[component]
            curr.name = component
        return curr

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.child.keys())
        curr = self.traverse(path)
        if curr.is_file:
            return [curr.name]
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.traverse(filePath)
        curr.is_file = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.traverse(filePath)
        return curr.content
