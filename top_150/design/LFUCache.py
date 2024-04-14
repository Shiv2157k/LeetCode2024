from collections import defaultdict
from typing import Optional


class DListNode:

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = DListNode()
        self.tail = DListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertToHead(self, node: DListNode) -> None:
        headNextNode = self.head.next
        node.next = headNextNode
        headNextNode.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove(self, node: DListNode) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self) -> Optional[DListNode]:
        lastNode = self.tail.prev
        self.remove(lastNode)
        return lastNode


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self.freqTable = defaultdict(DoublyLinkedList)
        self.minFreq = 0

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1

        node = self._cache[key]
        self.freqTable[node.freq].remove(node)

        if self.freqTable[node.freq].size == 0:
            if self.minFreq == node.freq:
                del self.freqTable[node.freq]
                self.minFreq += 1

        node.freq += 1
        self._cache[key] = node
        self.freqTable[node.freq].insertToHead(node)
        return node.val

    def put(self, key: int, val: int) -> None:

        if self._capacity == 0:
            return

        if key in self._cache:
            self._cache[key] = val
            self.get(key)
            return

        if self._capacity < len(self._cache):
            nodeToDel = self.freqTable[self.minFreq].removeTail()
            del self._cache[nodeToDel.key]

        newNode = DListNode(key, val)
        self.minFreq = 1
        self.freqTable[newNode.freq].insertToHead(newNode)
        self._cache[key] = newNode
