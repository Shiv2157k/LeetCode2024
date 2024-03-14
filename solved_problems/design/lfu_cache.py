from collections import defaultdict


class DListNode:

    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = DListNode(-1, -1)
        self.tail = DListNode(-1, -1)
        # link the head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_to_head(self, node: DListNode) -> None:
        head_next_node = self.head.next
        node.next = head_next_node
        head_next_node.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove(self, node: DListNode) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def remove_tail(self):
        last = self.tail.prev
        self.remove(last)
        return last


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._freq_table = defaultdict(DoublyLinkedList)
        self._min_freq = 0

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        # fetch the node
        node = self._cache[key]
        # remove the node from frequency table as it has got a new frequency now
        self._freq_table[node.freq].remove(node)
        # if there are no nodes left in the value associated with the freq key
        if self._freq_table[node.freq].size == 0:
            # clean it up from the table
            del self._freq_table[node]
            self._min_freq += 1
        node.freq += 1
        self._cache[key] = node
        self._freq_table[node.freq].insert_to_head(node)
        return node.val

    def put(self, key: int, value: int):
        # if the minimum capacity is zero
        if self._capacity == 0:
            return

        if key in self._cache:
            self._cache[key].val = value
            self.get(key)
            return
        # time to evict/ invalidate cache
        if self._capacity == len(self._cache):
            node_to_delete = self._freq_table[self._min_freq].remove_tail()
            del self._cache[node_to_delete.key]
        new_node = DListNode(key, value)
        # reset the min freq
        self._min_freq = 1
        self._freq_table[new_node.freq].insert_to_head(new_node)
        self._cache[key] = new_node