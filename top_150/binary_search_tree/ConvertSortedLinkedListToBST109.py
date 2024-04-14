from typing import Optional, List


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SortedLinkedList:

    def findMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # pointer that disconnects the left half
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # handle the case when slow is equal to None
        if prev:
            prev.next = None

        return slow

    def convertToBSTV0(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Approach: Find Mid
        T: O(N log N)
        S: O(log N)
        :param head:
        :return:
        """
        if not head:
            return None

        mid = self.findMiddleNode(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.convertToBSTV0(head)
        node.right = self.convertToBSTV0(mid.next)
        return node

    def _convertLinkedListToArray(self, node: Optional[ListNode]) -> List[int]:
        nums = []

        while node:
            nums.append(node.val)
            node = node.next
        return nums

    def convertToBSTV1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Approach: Trade Space Convert to List
        T: O(N)
        S: O(log N)
        :param head:
        :return:
        """

        if not head:
            return head

        def listToBSTConverter(left, right):

            if left > right:
                return None

            pivot = left + (right - left) // 2

            root = TreeNode(nums[pivot])

            root.left = listToBSTConverter(left, pivot - 1)
            root.right = listToBSTConverter(pivot + 1, right)
            return root

        nums = self._convertLinkedListToArray(head)
        return listToBSTConverter(0, len(nums) - 1)

    def convertToBSTV2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Approach: Inorder +
        T: O(N)
        S: O(log N)
        :param head:
        :return:
        """
        def _size(prev: Optional[ListNode]):
            length = 0
            while prev:
                prev = prev.next
                length += 1
            return length

        curr = head
        size = _size(curr)

        def convertToBST(left: int, right: int):
            nonlocal head
            # invalid case
            if left > right:
                return None

            pivot = left + (right - left) // 2
            # first step to simulate inorder traversal recursively from left half
            left = convertToBST(left, pivot - 1)

            # Once left half is traversed, process the current node
            root = TreeNode(head.val)
            root.left = left

            # maintain the invariance mentioned in the algorithm
            head = head.next

            # recurse on the right hand side and form BST out of them
            root.right = convertToBST(pivot + 1, right)
            return root
        return convertToBST(0, size - 1)
