from typing import Optional, Dict


class DListNode:

    def __init__(self, key: int = -1, val: int = -1, next: 'DListNode' = None, prev: 'DListNode' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._cache: Dict[int, DListNode] = {}
        self._head: DListNode = DListNode(-1, -1)
        self._tail: DListNode = DListNode(-1, -1)

        # connect head and tail
        self._head.next = self._tail
        self._tail.prev = self._head

    def _addNode(self, node: Optional[DListNode]) -> None:
        # will be adding nodes to tail
        prevNode = self._tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self._tail
        self._tail.prev = node

    def _removeNode(self, node: Optional[DListNode]) -> None:
        # will removing nodes from head
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]

        self._removeNode(node)
        self._addNode(node)

        return node.val

    def put(self, key: int, val: int) -> None:

        if key in self._cache:
            oldNode = self._cache[key]
            self._removeNode(oldNode)

        newNode = DListNode(key, val)
        self._addNode(newNode)
        self._cache[key] = newNode

        if self._capacity < len(self._cache):
            nodeToDel = self._head.next
            self._removeNode(nodeToDel)
            del self._cache[nodeToDel.key]
