from collections import deque
from typing import Optional



class Node:


    def __init__(self, val: int=-1, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTreeNext:

    def connectV0(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Queue BFS
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

    def processChildNodes(self, childNode: Optional[Node], prev: Optional[Node], leftMost: Optional[Node]) -> (Optional[Node], Optional[Node]):

        if childNode:

            if prev:
                prev.next = childNode
            else:
                leftMost = childNode
            prev = childNode
        return prev, leftMost

    def connectV1(self, root: Optional[Node]) -> Optional[Node]:
        """
        Approach: Without extra space
        T: O(N )
        S: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        leftmost = root
        while leftmost:

            prev, curr = None, leftmost

            leftmost = None

            while curr:

                prev, leftmost = self.processChildNodes(curr.left, prev, leftmost)
                prev, leftmost = self.processChildNodes(curr.right, prev, leftmost)

                curr = curr.next
        return root

