from heapq import heappush, heappop
from queue import PriorityQueue
from typing import Optional, List


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedLists:

    def mergeKSortedV1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Divide and Conquer Merge
        T: O(N log K)
        S: O(1)
        :param lists:
        :return:
        """
        interval = 1
        length = len(lists)

        while interval < length:

            for index in range(0, length - interval, interval * 2):
                lists[index] = self._mergeTwoSortedLists(lists[index], lists[index + 1])
            interval *= 2
        return lists[0] if length > 0 else None

    def _mergeTwoSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        T:O(N)
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """
        preHead = ListNode(-1)
        preview = preHead

        while l1 and l2:
            if l1.val <= l2.val:
                preview.next = l1
                l1 = l1.next
            else:
                preview.next = l2
                l2 = l2.next
            preview = preview.next

        preview.next = l1 if l1 is not None else l2
        return preHead.next

    def mergeKSortedV01(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Heapq
        T: O(N log K)
        S: O(K)
        :param lists:
        :return:
        """
        preHead = ListNode(-1)
        newNode = preHead

        minHeap = []

        for index, linkedNode in enumerate(lists):
            if linkedNode:
                heappush(minHeap, (linkedNode.val, index, linkedNode))

        while minHeap:

            val, index, currNode = heappop(minHeap)
            newNode.next = ListNode(val)
            newNode = newNode.next
            currNode = currNode.next

            if currNode:
                heappush(minHeap, (currNode.val, index, currNode))
        return preHead.next

    def mergeKSortedV0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Priority Queue
        T: O(N log K)
        S: O(K)
        :param lists:
        :return:
        """
        preHead = ListNode(-1)
        newNode = preHead

        pq = PriorityQueue()

        for index, linkedNode in enumerate(lists):
            if linkedNode:
                pq.put((linkedNode.val, index, linkedNode))

        while not pq.empty():
            val, index, currNode = pq.get()
            newNode.next = ListNode(val)
            newNode = newNode.next
            currNode = currNode.next
            if currNode:
                pq.put((currNode.val, index, currNode))
        return preHead.next
