from typing import Optional


class TreeNode:

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def tree_to_doubly_linked_list(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iteration Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        stack = []
        head = None
        tail = None

        while root or stack:

            while stack:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root:
                if tail:
                    tail.right = root
                    root.left = tail

                if not head:
                    head = root

                tail = root
                root = root.right
        head.left = tail
        tail.right = head
        return head
