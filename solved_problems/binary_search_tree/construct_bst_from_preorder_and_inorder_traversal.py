from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def construct_bst_from(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param preorder:
        :param inorder:
        :return:
        """
        # Step 2: Construction based on
        # preorder -> root->left->right
        # inorder -> left->root->right
        def preorder_to_bst(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_ptr
            # base case
            if left > right:  # reached leaf node
                return None

            root_value = preorder[preorder_ptr]
            preorder_ptr += 1
            root = TreeNode(root_value)

            # build the left and right tree
            root.left = preorder_to_bst(left, inorder_index_map[root_value] - 1)
            root.right = preorder_to_bst(inorder_index_map[root_value] + 1, right)

            return root

        # initialize preorder pointer
        preorder_ptr = 0
        # Step 1: Build inorder mapping to figure out left and right subtree
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return preorder_to_bst(0, len(preorder) - 1)
