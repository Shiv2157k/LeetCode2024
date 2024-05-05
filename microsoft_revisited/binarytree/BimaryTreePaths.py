from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Approach: Iterative DFS Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        paths: List[str] = []
        stack = [(root, str(root.val))]

        while stack:

            node, path = stack.pop()

            # if leaf add it to paths
            if not node.left and not node.right:
                paths.append(path)

            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths
