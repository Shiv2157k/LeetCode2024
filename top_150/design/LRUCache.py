class DLinkedNode:

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}

        self._head = DLinkedNode()
        self._tail = DLinkedNode()

        self._head.next = self._tail
        self._tail.prev = self._head

    def _add(self, node: DLinkedNode):

        prevNode = self._tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self._tail
        self._tail.prev = node

    def _remove(self, node: DLinkedNode):

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self._cache:
            old_node = self._cache[key]
            self._remove(old_node)

        newNode = DLinkedNode(key, value)
        self._cache[key] = newNode
        self._add(newNode)

        if self._capacity < len(self._cache):
            nodeToDel = self._head.next
            self._remove(nodeToDel)
            del self._cache[nodeToDel.key]
