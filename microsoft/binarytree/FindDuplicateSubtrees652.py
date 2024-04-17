from typing import Optional, List


class TreeNode:

    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def findDuplicateSubTree(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Approach: Inorder Traversal as key
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def traverse(node: Optional[TreeNode]) -> int:

            if not node:
                return 0

            # build the triplet as a tuple
            triplet = (traverse(node.left), node.val, traverse(node.right))

            # triplet doesn't exist add it into hashmap
            if triplet not in tripletToId:
                tripletToId[triplet] = len(tripletToId) + 1

            currId = tripletToId[triplet]
            # add currId into the freqMap
            freqMap[currId] = freqMap.get(currId, 0) + 1
            # check for duplicate
            if freqMap[currId] == 2:
                output.append(node)
            return currId

        output = []
        tripletToId = {}
        freqMap = {}
        traverse(root)
        return output