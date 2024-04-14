from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def recoverTreeV3(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        x, y = None, None
        pred = None

        while root:

            if root.left:

                predecessor = root.left

                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # build the link if no link
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:  # unlink and also set pred, x and y
                    # check for swapped nodes now
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

    def recoverTreeV2(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def recoverWithInorder(node: Optional[TreeNode]) -> None:
            nonlocal pred, x, y
            if not node:
                return

            recoverWithInorder(node.left)

            if pred and pred.val > node.val:
                y = node
                if not x:
                    x = pred
                else:
                    return
            pred = node
            recoverWithInorder(node.right)

        pred, x, y = None, None, None
        recoverWithInorder(root)
        x.val, y.val = y.val, x.val

    def recoverTreeV1(self, root: Optional[TreeNode]) -> None:
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
        x = y = predecessor = None

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if predecessor and predecessor.val > root.val:
                y = root
                if x is None:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right
        x.val, y.val = y.val, x.val

    def recoverTreeV0(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        # get the inorder list
        def inorder(node: Optional[TreeNode]) -> List[int]:
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        # find the nodes to be swapped
        def findNodesToBeSwapped(vals: List[int]) -> (int, int):
            x, y = None, None
            for index in range(len(vals) - 1):

                if vals[index + 1] < vals[index]:
                    y = vals[index + 1]

                    if x is None:
                        x = vals[index]
                    else:
                        break
            return x, y

        # recover the tree
        def recover(r: Optional[TreeNode], count: int):

            if r:

                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1

                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        nums = inorder(root)
        x, y = findNodesToBeSwapped(nums)
        return recover(root, 2)
