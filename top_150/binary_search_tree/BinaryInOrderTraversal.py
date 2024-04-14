from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def inOrderTraversalV0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        return self.inOrderTraversalV0(root.left) + [root.val] + self.inOrderTraversalV0(root.right) if root else []

    def inOrderTraversalV1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Iteration using stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = []
        result = []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def inOrderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Morris Traversal (Binary Threading)
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        curr = root
        pre = None
        result = []

        while curr:

            # if there is no left simply append val and move right
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                # move complete right i.e., predecessor node
                while pre.right:
                    pre = pre.right

                # now right side of leaf node thread it with curr
                pre.right = curr
                # store curr in temp
                temp = curr
                # move to the next left of the curr
                curr = curr.left
                # now break the link to avoid infinite loop
                temp.left = None
        return result
