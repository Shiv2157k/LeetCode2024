from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_right_side_view_v1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: BFS
        T: O(N)
        S: O(D)
        :param root:
        :return:
        """
        if not root:
            return []
        right_view = []
        queue = deque()
        queue.append(root)

        while queue:
            level = len(queue)
            for level_index in range(level):

                node = queue.popleft()
                # last index -> that is our right most node
                if level_index == level - 1:
                    right_view.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view

    def get_right_side_view_v0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: DFS
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """
        if not root:
            return []
        right_view = []

        def depth_first_search(node: Optional[TreeNode], level: int) -> None:
            if level == len(right_view):
                right_view.append(node.val)
            else:
                for child in [node.left, node.right]:
                    if child:
                        depth_first_search(child, level + 1)

        depth_first_search(root, 0)
        return right_view
