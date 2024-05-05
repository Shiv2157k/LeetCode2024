from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach:
        T: O(N)
        S: O(N)
        :param preorder:
        :param inorder:
        :return:
        """

        def build_arr_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx

            if left > right:
                return None

            root_val = preorder_idx[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)

            root.left = build_arr_to_tree(left, inorder_index_map[root_val] - 1)
            root.right = build_arr_to_tree(inorder_index_map[root_val] + 1, right)
            return root

        preorder_idx = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        return build_arr_to_tree(0, len(preorder) - 1)
