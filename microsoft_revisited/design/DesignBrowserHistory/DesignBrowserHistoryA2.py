class DListNode:

    def __init__(self, url: str, prev: 'DListNode' = None, next: 'DListNode' = None):
        self.data = url
        self.prev = prev
        self.next = next


class BrowserHistoryII:

    def __init__(self, homepage: str):
        self._head = DListNode(homepage)
        self._current = self._head

    def visit(self, url: str) -> None:

        new_node = DListNode(url)
        self._current.next = new_node
        new_node.prev = self._current

        self._current = new_node

    def back(self, steps: int) -> str:

        while steps and self._current.prev:
            self._current = self._current.prev
            steps -= 1
        return self._current.data

    def forward(self, steps: int) -> str:

        while steps and self._current.next:
            self._current = self._current.next
            steps -= 1
        return self._current.data
