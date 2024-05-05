from typing import Optional, Dict


class DoublyListNode:

    def __init__(self, key: int = -1, val: int = -1, next: 'DoublyListNode' = None, prev: 'DoublyListNode' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: Dict[int, DoublyListNode] = {}
        self._head = DoublyListNode(-1, -1)
        self._tail = DoublyListNode(-1, -1)

        # connect head and tail
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove_node(self, node: Optional[DoublyListNode]):
        # remove node from the head
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node(self, node: Optional[DoublyListNode]):

        prev_node = self._tail.prev
        node.prev = prev_node
        prev_node.next = node
        node.next = self._tail
        self._tail.prev = node

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._remove_node(node)
        self._add_node(node)
        return node.val

    def put(self, key: int, val: int) -> None:

        if key in self._cache:
            old_node = self._cache[key]
            self._remove_node(old_node)
        new_node = DoublyListNode(key, val)
        self._cache[key] = new_node
        self._add_node(new_node)

        if len(self._cache) > self._capacity:
            node_to_del = self._head.next
            self._remove_node(node_to_del)
            del self._cache[node_to_del.key]
