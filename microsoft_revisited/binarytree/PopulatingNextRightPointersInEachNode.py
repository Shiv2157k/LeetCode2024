from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTreeWithNext:

    def connectV1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iterative No extra space
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

                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left
        return root

    def connectV0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iterative BFS
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
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
