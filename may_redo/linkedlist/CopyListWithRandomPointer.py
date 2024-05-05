from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = val
        self.next = next
        self.random = random


class LinkedList:

    def __init__(self):
        self._visited = {}

    def copy_with_random_pointer_vo(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        if head in self._visited:
            return self._visited[head]

        clone_node = ListNode(head.val)
        self._visited[head] = clone_node

        clone_node.next = self.copy_with_random_pointer_vo(head.next)
        clone_node.random = self.copy_with_random_pointer_v0(head.random)
        return clone_node

    def copy_with_random_pointer_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        self._visited = {}
        old_node = head
        new_node = ListNode(old_node.val)
        self._visited[old_node] = new_node

        while old_node:
            new_node.random = self._fetch_cloned_node(old_node.random)
            new_node.next = self._fetch_cloned_node(old_node.next)

            new_node = new_node.next
            old_node = old_node.next
        return self._visited[head]

    def _fetch_cloned_node(self, node: Optional[ListNode]):

        if node:
            if node in self._visited:
                return self._visited[node]
            else:
                self._visited[node] = ListNode(node.val)
                return self._visited[node]
        return None

    def copy_with_random_pointer_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: O(N)
        S: O(1)
        :param head:
        :return:
        """
        # Step 1 and 2: Weave
        # Step 1: Build the link A -> A' -> B - B'...
        pointer = head

        while pointer:
            new_node = ListNode(pointer.val)
            new_node.next = pointer.next
            pointer.next = new_node
            pointer = new_node.next

        pointer = head
        # Step 2: Build the link for random
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next

        # Step 3: Un-weave
        old_ptr = head
        new_ptr = head.next
        new_head = head.next

        while old_ptr:
            old_ptr.next = old_ptr.next.next
            new_ptr.next = new_ptr.next.next if new_ptr.next else None

            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        return new_head
