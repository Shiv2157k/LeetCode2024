from queue import PriorityQueue
from heapq import heappop, heappush
from typing import List, Optional


class LinkedNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class KSortedLinkedLists:

    def mergeV1(self, lists: List[Optional[LinkedNode]]) -> Optional[LinkedNode]:
        """
        Approach: Intervals
        T: O(N * K)
        S: O(1)
        :param lists:
        :return:
        """
        k = len(lists)
        interval = 1
        while interval < k:
            for index in range(0, k - interval, interval * 2):
                lists[index] = self.__MergeTwoLists(lists[index], lists[index + interval])
            interval *= 2
        return lists[0] if k > 0 else None

    def __MergeTwoLists(self, l1: Optional[LinkedNode], l2: Optional[LinkedNode]) -> Optional[LinkedNode]:
        preHead = LinkedNode(-1)
        pointer = preHead

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        pointer.next = l1 if l1 else l2
        return preHead.next



    def mergeV01(self, lists: List[Optional[LinkedNode]]) -> Optional[LinkedNode]:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N * K)
        :param lists:
        :return:
        """

        preHead = LinkedNode()
        pointer = preHead
        minHeap = []

        for index, linkedNode in enumerate(lists):
            if linkedNode:
                heappush(minHeap, (linkedNode.val, index, linkedNode))

        while minHeap:
            val, index, node = heappop(minHeap)
            pointer.next = LinkedNode(val)
            pointer = pointer.next
            node = node.next
            if node:
                heappush(minHeap, (node.val, index, node))
        return preHead.next

    def mergeV0(self, lists: List[Optional[LinkedNode]]) -> Optional[LinkedNode]:
        """
        Approach: Priority Queue
        T: O(N log N)
        S: O(N * K)
        :param lists:
        :return:
        """

        pq = PriorityQueue()
        preHead = LinkedNode()
        pointer = preHead

        for index, linkedNode in enumerate(lists):
            if linkedNode:
                pq.put((linkedNode.val, index, linkedNode))

        while pq.not_empty:
            val, index, node = pq.get()
            pointer.next = LinkedNode(val)
            pointer = pointer.next
            node = node.next

            if node:
                pq.put((node.val, index, node))
        return preHead.next
