from typing import Optional


class RandomListNode:

    def __init__(self, val: int = -1, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class RandomLinkedList:

    def __init__(self):
        self._visited_map = {}

    def clone_v2(self, head: Optional[RandomListNode]) -> Optional[RandomListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :return:
        """
        if not head:
            return head

        pointer = head
        # Step 1: Weave the next pointer to the current random linked list
        while pointer:
            new_node = RandomListNode(pointer.val, None, None)
            new_node.next = pointer.next  # 1
            pointer.next = new_node  # 2
            pointer = new_node.next  # 3
            # already doing in step 1 pointer = pointer.next

        pointer = head
        # Step 2: Weave the random pointer to the current random linked list
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next

        # Step 3: Un-weave old and new random linked list to make it a clone
        old_pointer_list = head
        new_pointer_list = head.next
        new_head = head.next
        while old_pointer_list:
            old_pointer_list.next = old_pointer_list.next.next
            new_pointer_list.next = new_pointer_list.next.next if new_pointer_list.next else None
            old_pointer_list = old_pointer_list.next
            new_pointer_list = new_pointer_list.next
        return new_head

    def clone_v1(self, head: Optional[RandomListNode]) -> Optional[RandomListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :return:
        """
        if not head:
            return head
        self._visited_map = {}

        old_node = head
        new_node = RandomListNode(old_node.val, None, None)
        self._visited_map[old_node] = new_node

        while old_node:
            new_node.random = self._get_node(old_node.random)
            new_node.next = self._get_node(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self._visited_map[head]

    def _get_node(self, node: Optional[RandomListNode]) -> Optional[RandomListNode]:
        if node:
            if node in self._visited_map:
                return self._visited_map[node]
            else:
                new_node = RandomListNode(node.val, None, None)
                self._visited_map[node] = new_node
                return self._visited_map[node]
        return None

    def clone_v0(self, head: Optional[RandomListNode]) -> Optional[RandomListNode]:
        """
        Recursion
        T: O(N)
        S: O(N)
        :return:
        """
        # base case
        if not head:
            return head
        if head in self._visited_map:
            return self._visited_map[head]
        # clone the node
        node = RandomListNode(head.val, None, None)
        # add it into the mapper
        self._visited_map[head] = node

        node.random = self.clone_v0(head.random)
        node.next = self.clone_v0(head.next)

        return self._visited_map[head]  # return node
