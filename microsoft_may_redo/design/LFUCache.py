from typing import Dict


class DoublyListNode:

    def __init__(self, key: int, val: int, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 1


class DoublyLinkedList:

    def __init__(self):
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: DoublyListNode):
        next_node = self.head.next
        next_node.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        self.size += 1

    def remove_node(self, node: DoublyListNode):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def remove_tail(self) -> DoublyListNode:
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node


class LFUCache:

    def __init__(self, capacity: int):
        self.__capacity: int = capacity
        self.__freq_map: Dict[int, DoublyLinkedList] = {}
        self.__cache: Dict[int, DoublyListNode] = {}
        self.__min_freq: int = 1

    def get(self, key: int) -> int:

        if key not in self.__cache:
            return -1

        node = self.__cache[key]
        self.__freq_map[node.freq].remove_node(node)

        if self.__freq_map[node.freq].size == 0:
            del self.__freq_map[node.freq]
            if node.freq == self.__min_freq:
                self.__min_freq += 1

        node.freq += 1
        self.__cache[key] = node
        self.__freq_map[node.freq] = self.__freq_map.get(node.freq, DoublyLinkedList())
        self.__freq_map[node.freq].add_node(node)
        return node.val

    def put(self, key: int, val: int) -> None:

        if self.__capacity == 0:
            return

        if key in self.__cache:
            self.__cache[key].val = val
            self.get(key)
            return

        if self.__capacity == len(self.__cache):
            node_to_del = self.__freq_map[self.__min_freq].remove_tail()
            del self.__cache[node_to_del.key]

        new_node = DoublyListNode(key, val)
        self.__min_freq = 1
        self.__freq_map[new_node.freq] = self.__freq_map.get(new_node.freq, DoublyLinkedList())
        self.__freq_map[new_node.freq].add_node(new_node)
        self.__cache[key] = new_node
