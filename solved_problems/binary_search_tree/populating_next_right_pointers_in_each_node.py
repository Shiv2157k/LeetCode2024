from collections import deque
from typing import Optional


class BSTNode:

    def __init__(self, val: int = -1):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class BalancedBinarySearchTree:

    def connect_same_level_nodes_v1(self, root: Optional[BSTNode]) -> Optional[BSTNode]:
        """
        Approach: In-place link building
        T: O(N)
        T: O(1)
        :param root:
        :return:
        """
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # case 1: from level 1 building link of level 2
                head.left.next = head.right
                # case 2: if we are not on the complete right
                # where we check
                if head.next:
                    # build the right node connection
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    def connect_same_level_nodes_v0(self, root: Optional[BSTNode]) -> Optional[BSTNode]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        queue = deque()
        deque.append(root)
        while queue:
            # this is used to mark a level
            size = len(queue)
            for index in range(size):
                node = queue.popleft()
                # connecting the link between same level nodes
                if index < size - 1:
                    node.next = queue[0]
                # appending left and right nodes of same level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
