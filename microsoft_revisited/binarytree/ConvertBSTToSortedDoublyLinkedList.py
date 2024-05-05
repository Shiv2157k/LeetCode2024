from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def tree_to_sorted_doubly_linked_list_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        stack: List[TreeNode] = []
        first: Optional[TreeNode] = None
        last: Optional[TreeNode] = None

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root:

                if last:
                    last.right = root
                    root.left = last
                else:
                    first = root

                last = root
                root = root.right
        first.left = last
        last.right = first
        return first

    def tree_to_sorted_doubly_linked_list(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return root

        def in_order(node: Optional[TreeNode]) -> None:
            nonlocal first, last

            in_order(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node

            last = node
            in_order(node.right)

        first: Optional[TreeNode] = None
        last: Optional[TreeNode] = None
        in_order(root)
        first.left = last
        last.right = first
        return first
