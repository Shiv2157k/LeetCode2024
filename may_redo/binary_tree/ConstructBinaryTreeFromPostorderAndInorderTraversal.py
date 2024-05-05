from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Approach: simulation
        T: O(N)
        S: O(N)
        :param inorder:
        :param postorder:
        :return:
        """

        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_ptr

            if left > right:
                return None

            root_val = postorder[postorder_ptr]
            postorder_ptr -= 1
            root = TreeNode(root_val)
            # post order logic construct right and then left
            root.right = helper(inorder_ptr_map[root_val] + 1, right)
            root.left = helper(left, inorder_ptr_map[root_val] - 1)
            return root

        postorder_ptr = len(postorder) - 1
        inorder_ptr_map = {}

        for ptr, val in enumerate(inorder):
            inorder_ptr_map[val] = ptr
        return helper(0, len(inorder) - 1)
