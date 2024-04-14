from typing import Optional
from collections import deque


class Node:

    def __init__(self, val: int = -1, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class RandomPointerLinkedNodes:

    def __init__(self):
        self.visitedHash = {}

    def copyRandomListV2(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: with no extra space
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head:
            return head

        ptr = head
        while ptr:
            clonedNode = Node(ptr.val, None, None)
            clonedNode.next = ptr.next
            ptr.next = clonedNode
            ptr = clonedNode.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        oldPtr = head
        newPtr = head.next
        newHead = head.next

        while oldPtr:
            oldPtr = oldPtr.next.next
            newPtr = newPtr.next.next if newPtr.next else None

            oldPtr = oldPtr.next
            newPtr = newPtr.next
        return newHead

    def copyRandomListV0(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """
        self.visitedHash = {}
        if head == None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        clonedNode = Node(head.val, None, None)

        self.visitedHash[head] = clonedNode

        clonedNode.next = self.copyRandomListV0(head.next)
        clonedNode.random = self.copyRandomListV0(head.random)

        return clonedNode

    def copyRandomListV1(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head:
            return head

        oldNode = head
        newNode = Node(oldNode.val, None, None)
        self.visitedHash = {oldNode: newNode}
        queue = deque([oldNode])

        while oldNode:
            newNode.random = self.getClonedNode(oldNode.random)
            newNode.next = self.getClonedNode(oldNode.next)

            oldNode = oldNode.next
            newNode = newNode.next
        return self.visitedHash[head]

    def getClonedNode(self, node):

        if node:

            if node in self.visitedHash:
                return self.visitedHash[node]
            else:
                self.visitedHash[node] = Node(node.val, None, None)
                return self.visitedHash[node]
        return None
