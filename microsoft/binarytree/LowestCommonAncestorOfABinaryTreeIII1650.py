from typing import Optional


class Node:

    def __init__(self, val: int = -1):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:

    def lowestCommonAncestorV0(self, p: Optional[Node], q: Optional[Node]) -> Optional[Node]:
        """
        Approach: HashSet
        T: O(N)
        S: O(H)
        :param p:
        :param q:
        :return:
        """

        seen = set()
        while p:
            seen.add(p)
            p = p.parent

        while q:
            if q in seen:
                return q
            q = q.parent
        return None

    def lowestCommonAncestorV1(self, p: Optional[Node], q: Optional[Node]) -> Optional[Node]:
        """
        Approach: HashSet
        T: O(H)
        S: O(1)
        :param p:
        :param q:
        :return:
        """

        def getHeight(node: Optional[Node]) -> int:
            height = 0
            while node:
                node = node.parent
                height += 1
            return height

        h1 = getHeight(p)
        h2 = getHeight(q)

        if h1 < h2:
            p, q = q, p

        heightDiff = abs(h1 - h2)

        while heightDiff > 0:
            p = p.parent
            heightDiff -= 1

        while p != q:
            p = p.parent
            q = q.parent
        return p

    def lowestCommonAncestorV3(self, p: Optional[Node], q: Optional[Node]) -> Optional[Node]:
        """
        Approach: HashSet
        T: O(h1 + h2)
        S: O(1)
        :param p:
        :param q:
        :return:
        """
        runner1, runner2 = p, q

        while runner1 != runner2:
            runner1 = runner1.parent if runner1 else q
            runner2 = runner2.parent if runner2 else p
        return runner1
