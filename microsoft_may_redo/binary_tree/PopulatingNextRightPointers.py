from collections import deque
from typing import Optional


class Node:

    def __init__(self, val: int = -1, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTree:

    def connect_v1(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Traversal without extra space
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        leftmost = root

        while leftmost:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    def connect_v0(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: BFS level order
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
                if i != size - 1:
                    node.next = queue[0]
                queue.append(node.left)
                queue.append(node.right)
        return root
