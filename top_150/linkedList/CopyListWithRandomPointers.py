from typing import Optional


class Node:

    def __init__(self, val: int = -1, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class LinkedList:

    def __init__(self):
        self.visited = {}

    def cloneListV2(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: Iterative No extra space
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head:
            return head

        # Step 1: build/ weave the link for next pointers
        ptr = head

        while ptr:
            clonedNode = Node(ptr.val, None, None)

            clonedNode.next = ptr.next
            ptr.next = clonedNode
            ptr = clonedNode.next

        # Step 3: build/ weave link for random pointers
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Step 4: Separate out the cloned and original nodes
        oldPtr = head
        newPtr = head.next
        newHead = head.next

        while oldPtr:
            oldPtr.next = oldPtr.next.next
            newPtr.next = newPtr.next.next if newPtr.next else None

            oldPtr = oldPtr.next
            newPtr = newPtr.next
        return newHead


    def cloneListV0(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head:
            return head

        if head in self.visited:
            return self.visited[head]

        cloneNode = Node(head.val)

        cloneNode.next = self.cloneListV0(head.next)
        cloneNode.random = self.cloneListV0(head.random)

        return cloneNode

    def cloneListV1(self, head: Optional[Node]) -> Optional[Node]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head:
            return head

        self.visited = {}
        oldNode = head
        newNode = Node(head.val)
        self.visited = {oldNode: newNode}

        while oldNode:

            newNode.next = self._getClonedNode(oldNode.next)
            newNode.random = self._getClonedNode(oldNode.random)

            newNode = newNode.next
            oldNode = oldNode.next
        return self.visited[head]

    def _getClonedNode(self, node: Optional[Node]) -> Optional[Node]:
        if node:
            if node in self.visited:
                return self.visited[node]
            self.visited[node] = Node(node.val)
            return self.visited[node]
        return None

