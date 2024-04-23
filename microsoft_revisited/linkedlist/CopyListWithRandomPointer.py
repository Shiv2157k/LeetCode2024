from typing import Optional, Dict


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = val
        self.next = next
        self.random = random


class LinkedListWithRandomPointer:


    def copyRandomListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iterative O(1)
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head:
            return head

        ptr = head

        # Step 1: weave next pointers A -> A' -> B -> B'
        while ptr:
            newNode = ListNode(ptr.val, None, None)
            newNode.next = ptr.next
            ptr.next = newNode
            ptr = newNode.next

        # Step 2: weave random pointers
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # un-weave and separate old and new
        oldPtr = head
        newHead = head.next
        newPtr = head.next

        while oldPtr:
            oldPtr.next = oldPtr.next.next
            newPtr.next = newPtr.next.next if newPtr.next else None
            oldPtr = oldPtr.next
            newPtr = newPtr.next
        return newHead



    def copyRandomListV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        # validation
        if not head:
            return head

        visited: Dict[ListNode, ListNode] = {}
        oldNode: ListNode = head
        newNode: ListNode = ListNode(oldNode.val, None, None)
        visited[oldNode] = newNode

        while oldNode:

            newNode.random = self._fetchClonedNode(oldNode.random, visited)
            newNode.next = self._fetchClonedNode(oldNode.next, visited)

            oldNode = oldNode.next
            newNode = newNode.next
        return visited[head]

    def _fetchClonedNode(self, node: Optional[ListNode], visited: Dict[ListNode, ListNode]) -> Optional[ListNode]:
        if node:
            if node in visited:
                return visited[node]
            else:
                visited[node] = ListNode(node.val, None, None)
                return visited[node]
        return None

    def copyRandomListV0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """
        if not head:
            return head

        def cloneList(node: Optional[ListNode]):
            # base case
            if not node:
                return None
            if node in visited:
                return visited[node]

            cloneNode = ListNode(node.val, None, None)

            visited[node] = cloneNode

            cloneNode.random = cloneList(node.random)
            cloneNode.next = cloneList(node.next)

            return cloneNode

        visited = {}
        cloneList(head)

        return visited[head]
