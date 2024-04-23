class DoublyLinkedList:

    def __init__(self, url: str, next=None, prev=None):
        self.data = url
        self.next = next
        self.prev = prev


class BrowserHistoryA2:

    def __init__(self, homepage: str):
        self._head = DoublyLinkedList(homepage)
        self._current = self._head

    def visit(self, url: str):

        newNode = DoublyLinkedList(url)
        self._current.next = newNode
        newNode.prev = self._current
        self._current = newNode

    def back(self, steps: int) -> str:

        while steps > 0 and self._current.prev:
            self._current = self._current.prev
            steps -= 1
        return self._current.data

    def forward(self, steps: int) -> str:
        while steps > 0 and self._current.next:
            self._current = self._current.next
            steps -= 1
        return self._current.data
