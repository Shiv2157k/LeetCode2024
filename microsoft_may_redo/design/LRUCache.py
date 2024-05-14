class DoublyListNode:

    def __init__(self, key: int = -1, val: int = -1, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):

        self.__capacity = capacity
        self.__cache = {}
        self.__head = DoublyListNode(-1, -1)
        self.__tail = DoublyListNode(-1, -1)

        # build the link
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    # helper add and remove nodes
    def __add_node(self, node: 'DoublyListNode') -> None:
        """
        Helper function to add nodes before tail
        """
        prev_node = self.__tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.__tail
        self.__tail.prev = node

    def __remove_node(self, node: 'DoublyListNode') -> None:
        """
        Helper function to remove nodes next to head
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        if key not in self.__cache:
            return -1

        node = self.__cache[key]
        self.__remove_node(node)
        self.__add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.__cache:
            old_node = self.__cache[key]
            self.__remove_node(old_node)

        new_node = DoublyListNode(key, value)
        self.__cache[key] = new_node
        self.__add_node(new_node)

        if len(self.__cache) > self.__capacity:
            node_to_del = self.__head.next
            self.__remove_node(node_to_del)
            del self.__cache[node_to_del.key]
