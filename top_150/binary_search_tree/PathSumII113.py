from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def _recurseTree(self, node: Optional[TreeNode], remainSum, path: List[int], pathList: List[List[int]]) -> None:

        if not node:
            return  # back track

        path.append(node.val)

        if not node.left and not node.right and remainSum == node.val:
            pathList.append(list(path))
        else:

            self._recurseTree(node.left, remainSum - node.val, path, pathList)
            self._recurseTree(node.right, remainSum - node.val, path, pathList)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N^2)
        S: O(N)
        :param root:
        :param targetSum:
        :return:
        """

        pathList = []
        self._recurseTree(root, targetSum, [], pathList)
        return pathList


if __name__ == "__main__":
    r = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                 TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))

    bst = BinaryTree()
    print(bst.pathSum(r, 22))
