from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedNodes:

    def reverseBetweenV1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param head:
        :param left:
        :param right:
        :return:
        """
        preHead = ListNode(-1, head)
        leftTail = preHead

        # traverse until the left tail that is node before left
        for _ in range(1, left):
            leftTail = leftTail.next

        # after the traverse this will be the reverse Head
        revHead = leftTail
        rightHead = leftTail.next

        # we reach until the node where right is pointed at the same time we reverse -> revHead
        # as well as the nodes after the right pointer -> rightHead
        for _ in range(left, right + 1):
            nextNode = rightHead.next
            rightHead.next = revHead
            revHead = rightHead
            rightHead = nextNode

        # link the tail of the reverse node with the right head
        leftTail.next.next = rightHead
        # link the tail of left with the reverse node head
        leftTail.next = revHead
        return preHead.next

    def reverseBetweenV0(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :param left:
        :param right:
        :return:
        """
        if not head:
            return None

        leftPrev, rightPrev = head, head
        stop = False

        def recurseAndReverse(rightPrev, left, right):

            nonlocal leftPrev, stop
            # base case. Don't proceed any further
            if right == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            rightPrev = rightPrev.next

            if left > 1:
                leftPrev = leftPrev.next

            # Recurse with left and right reduced.
            recurseAndReverse(rightPrev, left - 1, right - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if leftPrev == rightPrev or rightPrev.next == leftPrev:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                # reverse
                leftPrev.val, rightPrev.val = rightPrev.val, leftPrev.val
                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                leftPrev = leftPrev.next
        recurseAndReverse(rightPrev, left, right)
        return head
