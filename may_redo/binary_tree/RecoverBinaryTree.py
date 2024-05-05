from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def recover_v2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        x, y, pred = None, None, None

        while root:

            if root.left:

                predecessor = root.left
                while predecessor and predecessor.right != root:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = None
                    root = root.left
                else:

                    if pred and pred.val > root.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right
            else:

                if pred and pred.val > root.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val

    def recover_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iterative Inorder Traversal
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        stack = []

        x, y, pred = None, None, None

        while stack or root:

            while root:
                stack.append(root.val)
                root = root.left

            root = stack.pop()

            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val

    def recover_v0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def inorder(node: TreeNode) -> List[int]:
            return inorder(node.left) + [root.val] + inorder(node.right) if node else []

        def find_two_swapped(nums: List[int]) -> (int, int):
            size = len(nums)
            x = y = None

            for i in range(size - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover_tree(node: TreeNode, count: int):

            if node:
                if node.val == x or node.val == y:
                    node.val = x if node.val == y else y
                    count -= 1
                    if count == 0:
                        return
                recover_tree(node.left, count)
                recover_tree(node.right, count)

        nums = inorder(root)
        x, y = find_two_swapped(nums)
        return recover_tree(root, 2)
