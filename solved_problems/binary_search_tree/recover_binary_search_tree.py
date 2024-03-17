from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def recover_v3(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Morris Traversal
        Case 1: Find Predecessor, build link b/w predecessor and root
        Case 2: Find Predecessor, build already exists break the link
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        x = y = pred = None

        while root:

            if root.left:

                # find the predecessor
                # build the link if there is no link
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # build link if it is not there
                if predecessor.right is None:
                    predecessor.right = root
                    # go to left
                    root = root.left
                # break the link and also make out two swap nodes
                else: # predecessor.right == root:

                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root
                    predecessor.right = None
                root = root.right
            elif root.right:
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val

    def recover_v2(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Recursive Inorder with Node Swap
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def find_two_swap_nodes(root: TreeNode):
            nonlocal x, y, pred

            if not root:
                return

            find_two_swap_nodes(root.left)
            if not pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    return
            pred = root
            find_two_swap_nodes(root.right)

        x = y = pred = None
        find_two_swap_nodes(root)
        x.val, y.val = y.val, x.val

    def recover_v1(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Iterative Inorder
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = []
        x = y = pred = None
        # inorder iterative
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            # pop the left most node
            root = stack.pop()

            # parent of the root to find two swap nodes
            # which are in bad alignment
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val

    def recover_v0(self, root: Optional[TreeNode]) -> None:
        """
        Approach: Sort out in order list
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        # Step 1: Perform inorder
        def in_order(root: Optional[TreeNode]) -> List[int]:
            return in_order(root.left) + [root.val] + in_order(root.right)

        # Step 2: Get the nodes to be swapped
        def figure_nodes_to_swap(nums: List[int]) -> [int, int]:

            x = y = None
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y

        # Step 3: Recover BST
        def recover_bst(node: Optional[TreeNode], count: int):
            if node:
                recover_bst(node.left, count)
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover_bst(node.left, count)
                recover_bst(node.right, count)

        nums = in_order(root)
        x, y = figure_nodes_to_swap(nums)
        recover_bst(root, 2)
