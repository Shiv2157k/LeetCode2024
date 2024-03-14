class DoublyLinkedNode:

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # holds LRU cache capacity value
        self._capacity = capacity
        # to check whether given key exists and track the keys
        self._cache = dict()
        # dummy head and tail nodes for handling edge cases
        # i.e., when a doubly linked node is empty we do not have to
        # manage setting the head and tail everytime and
        # have a validation to check whether doubly linked node is empty or not
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode()

        # connect the dummy head and tail
        self._head.next = self._tail
        self._tail.prev = self._head

    def _add(self, node: DoublyLinkedNode):
        """
        Helper method to handle adding the node to end of the doubly linked list
        i.e., before the dummy tail
        :param node:
        :return:
        """
        prev_node = self._tail.prev
        prev_node.next = node
        node.next = self._tail
        node.prev = prev_node
        self._tail.prev = node

    def _remove(self, node: DoublyLinkedNode):
        """
        Helper method to handle remove of the node right after the head
        :param node:
        :return:
        """
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        # if the key does not exist in our cache return -1
        if key not in self._cache:
            return -1

        # key is present
        node = self._cache[key]
        # update the position of the node as it is used
        # we do this by removing and adding the node to the tail
        self._remove(node)
        self._add(node)
        # return node value
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key exists in our cache
        # remove the old node
        if key in self._cache:
            old_node = self.cache[key]
            self._remove(old_node)

        # add the updated or new node
        new_node = DoublyLinkedNode(key, value)
        # update in our cache map
        self._cache[key] = new_node
        self._add(new_node)

        # check capacity limit
        if len(self._cache) > self._capacity:
            node_to_del = self._head.next
            self._remove(node_to_del)
            # also clear it from the cache
            del self._cache[node_to_del.key]


if __name__ == "__main__":
    lru = LRUCache(5)
    lru.put(19, 7)
    lru.put(20, 5)
    lru.put(23, 5)
    lru.put(7, 9)
    lru.put(10, 7)
    print(lru.get(19))
    print(lru.get(7))
    print(lru.get(13))
    lru.put(6, 7)
    print(lru.get(6))
