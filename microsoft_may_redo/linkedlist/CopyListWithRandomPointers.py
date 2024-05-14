from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = val
        self.next = next
        self.random = random


class LinkedListWithRandomPointer:
    visited = {}

    def copy_list_with_random_pointer_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Without extra space
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head or head.next:
            return head

        # create and weave the clone node next pointer
        # A -> A' -> B -> B'
        pointer = head
        while pointer:
            clone_node = ListNode(pointer.val)
            clone_node.next = pointer.next
            pointer.next = clone_node
            pointer = clone_node.next

        # weave random pointers
        pointer = head
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next

        new_head = head.next
        old_ptr = head
        new_ptr = head.next

        # un-weave
        while old_ptr:
            old_ptr.next = old_ptr.next.next
            new_ptr.next = new_ptr.next.next if new_ptr.next else None

            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        return new_head

    def copy_list_with_random_pointer_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iteration
        T: O()
        S: O()
        :param head:
        :return:
        """
        if not head:
            return None

        old_node = head
        clone_node = ListNode(old_node.val, None, None)
        self.visited = {}
        self.visited = {old_node: clone_node}

        while old_node:
            clone_node.random = self.__fetch_cloned_node(old_node.random)
            clone_node.next = self.__fetch_cloned_node(old_node.next)

            old_node = old_node.next
            clone_node = clone_node.next

        return self.visited[head]

    def __fetch_cloned_node(self, node: Optional[ListNode]):

        if node:

            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = ListNode(node.val)
                return self.visited[node]
        return None

    def copy_list_with_random_pointer_v0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        :param head:
        :return:
        """
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        clone_node = ListNode(head.val, None, None)
        self.visited[head] = clone_node

        clone_node.next = self.copy_list_with_random_pointer_v0(head.next)
        clone_node.random = self.copy_list_with_random_pointer_v1(head.random)
        return clone_node
