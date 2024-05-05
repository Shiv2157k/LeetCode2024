from typing import Optional, Dict, DefaultDict
from collections import defaultdict


class DLinkedNode:

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1


class DLinkedList:

    def __init__(self):
        self.size = 0
        self.head = DLinkedNode(-1, -1)
        self.tail = DLinkedNode(-1, -1)

        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Optional[DLinkedNode]):
        # will always be adding nodes to the head
        next_to_head = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next = next_to_head
        next_to_head.prev = node
        self.size += 1

    def remove_node(self, node: Optional[DLinkedNode]):
        # will remove the node provided
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def remove_tail(self) -> Optional[DLinkedNode]:
        # will remove the node before dummy tail and
        # return it
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._cache: Dict[int, DLinkedNode] = {}
        # self._freq_map: DefaultDict[int, DLinkedList] = defaultdict(DLinkedList)
        self._freq_map: Dict[int, DLinkedList] = {}
        self._min_freq: int = 1

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._freq_map[node.freq].remove_node(node)

        if node.freq == self._min_freq and self._freq_map[node.freq].size == 0:
            del self._freq_map[node.freq]
            self._min_freq += 1

        node.freq += 1
        self._cache[key] = node
        self._freq_map[node.freq] = self._freq_map.get(node.freq, DLinkedList())
        self._freq_map[node.freq].add_node(node)
        return node.val

    def put(self, key: int, val: int) -> None:

        if self._capacity == 0:
            return

        if key in self._cache:
            self._cache[key].val = val
            self.get(key)
            return

        if self._capacity == len(self._cache):
            node_to_del = self._freq_map[self._min_freq].remove_tail()
            del self._cache[node_to_del.key]
        new_node = DLinkedNode(key, val)
        self._min_freq = 1
        # self._freq_map[new_node.freq] = self._freq_map.get(new_node.freq, DLinkedList())
        self._freq_map[new_node.freq].add_node(new_node)
        self._cache[key] = new_node

