from queue import PriorityQueue
from heapq import heappush, heappop
from typing import Optional, List


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def mergeKSortedListsV1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Divide and Conquer
        T: O(N log K)
        S: O(1)
        :param lists:
        :return:
        """

        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        interval = 1

        while interval < len(lists):

            for i in range(0, len(lists) - interval, interval * 2):
                # length = 4: (0, 1) -> (2, 3) -> (0, 2)
                lists[i] = self.mergeTwoSortedList(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def mergeTwoSortedList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        preHead = ListNode(-1)
        prev = preHead

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2

        return preHead.next

    def mergeKSortedListsV0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Heap
        T: O(N log K)
        S: O(N) Heap: O(K)
        :param lists:
        :return:
        """

        if not lists or len(lists) == 0:
            return None

        minHeap = []

        for index, listNode in enumerate(lists):
            if listNode:
                heappush(minHeap, (listNode.val, index, listNode))

        preHead = ListNode(-1)
        prev = preHead

        while minHeap:
            val, index, node = heappop(minHeap)

            prev.next = ListNode(val)
            prev = prev.next

            if node.next:
                heappush(minHeap, (node.next.val, index, node.next))
        return preHead.next

    def mergeKSortedListsV00(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Priority Queue
        T: O(N log K)
        S: O(N) PQ: O(K)
        :param lists:
        :return:
        """

        if not lists or len(lists) == 0:
            return None

        preHead = ListNode(-1)
        prev = preHead

        pq = PriorityQueue()

        for index, listNode in enumerate(lists):
            if listNode:
                pq.put((listNode.val, index, listNode))

        while not pq.empty():

            val, index, node = pq.get()

            prev.next = ListNode(val)
            prev = prev.next

            if node.next:
                pq.put((node.next.val, index, node.next))
        return preHead.next
