from typing import Optional
from collections import defaultdict


class DLinkedNode:

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class DLinkedList:

    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.size = 0

        # build head <-> tail connection
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node: Optional[DLinkedNode]):
        nextNode = self.head.next
        node.next = nextNode
        nextNode.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove(self, node: Optional[DLinkedNode]):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self) -> DLinkedNode:
        lastNode = self.tail.prev
        self.remove(lastNode)
        return lastNode


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._freqMap = defaultdict(DLinkedList)
        self._cache = {}
        self._minFreq = 0

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._freqMap[node.freq].remove(node)

        if node.freq == self._minFreq and self._freqMap[node.freq].size == 0:
            del self._freqMap[node.freq]
            self._minFreq += 1
        node.freq += 1
        self._freqMap[node.freq].addToHead(node)
        self._cache[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:

        if self._capacity == 0:
            return

        if key in self._cache:
            self._cache[key].val = value
            self.get(key)
            return

        if self._capacity <= len(self._cache):
            nodeToDel = self._freqMap[self._minFreq].removeTail()
            del self._cache[nodeToDel.key]
        newNode = DLinkedNode(key, value)
        self._minFreq = 1
        self._freqMap[newNode.freq].addToHead(newNode)
        self._cache[key] = newNode

