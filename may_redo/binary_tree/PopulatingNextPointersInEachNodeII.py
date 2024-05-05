from typing import Optional
from collections import deque



class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTreeWithNextPointers:

    def connect_v2(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Without extra space better version
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
            # resetting for next level
            head = dummy.next
            prev = dummy
            dummy.next = None
        return root
    def connect_v1(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Without extra space
        T: O(N)
        s: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        leftmost = root

        while leftmost:
            prev, curr = None, leftmost
            while curr:
                prev, leftmost = self._process_child(curr.left, prev, leftmost)
                prev, leftmost = self._process_child(curr.right, prev, leftmost)

                curr = curr.next
        return root

    def _process_child(self, child_node: Optional[Node], prev, leftmost) -> Optional[Node]:

        if child_node:

            if prev:
                prev.next = child_node
            else:
                leftmost = child_node
            prev = child_node
        return prev, leftmost
    def connect_vo(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Level Order Traversal
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
