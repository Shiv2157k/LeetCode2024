from collections import deque
from typing import Optional


class Node:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def connectV1(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # connection 1: left => right of same parent
                head.left.next = head.right
                # connection 2: b/ w different parents right and left child
                if head.next:
                    head.right.next = head.next.left
                # move to same level node
                head = head.next
            leftmost = leftmost.left
        return root

    def connectV0(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Iteration (BSF - Queue)
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

            for index in range(size):

                node = queue.popleft()

                if index < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
