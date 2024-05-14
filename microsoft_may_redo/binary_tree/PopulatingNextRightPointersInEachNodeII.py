from typing import Optional
from collections import deque


class Node:

    def __init__(self, val: int = -1, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTree:

    def populating_next_right_pointers_v1(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Iteration without extra space
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        dummy = Node(-1)
        prev = dummy
        head = root

        while head:

            while head:

                if head.left:
                    prev.next = head.left
                    prev = prev.next
                if head.right:
                    prev.next = head.right
                    prev = prev.next
                head = head.next
            head = dummy.next
            prev = dummy
            dummy.next = None
        return root

    def populating_next_right_pointers_v0(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Queue
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        queue = deque[(root)]

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if i != size - 1:
                    node.next = queue[0]

                for child_node in (node.left, node.right):
                    if child_node:
                        queue.append(child_node)
        return root