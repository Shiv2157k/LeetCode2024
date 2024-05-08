from typing import Optional, List
from queue import PriorityQueue
from heapq import heappop, heappush


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Merge with Divide and Conquer
        T: O(N log K)
        S: O(1)
        :param lists:
        :return:
        """
        if not lists or len(lists) == 0:
            return None

        if len(lists) <= 1:
            return lists[0]

        interval = 1

        while interval < len(lists):

            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self._merge_two_sorted_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def _merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        pre_head = ListNode(-1)
        prev = pre_head

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 or l2
        return pre_head.next

    def merge_k_lists_v1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Priority Queue
        T: O(N log K)
        S: O(n) & O(k)
        :param lists:
        :return:
        """

        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        pq = PriorityQueue()
        pre_head = ListNode(-1)
        prev = pre_head

        for index, node in enumerate(lists):
            if node:
                pq.put((node.val, index, node))

        while not pq.empty():

            val, index, node = pq.get()
            prev.next = ListNode(val)
            prev = prev.next

            if node.next:
                pq.put((node.next.val, index, node.next))
        return pre_head.next

    def merge_k_lists_v0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Min Heap
        T: O(N log K)
        S: O(n) & O(k)
        :param lists:
        :return:
        """

        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        min_heap = []
        pre_head = ListNode(-1)
        prev = pre_head

        for index, linked_list in enumerate(lists):
            if linked_list:
                heappush(min_heap, (linked_list.val, index, linked_list))

        while min_heap:
            val, index, node = heappop(min_heap)
            prev.next = ListNode(val)
            prev = prev.next

            if node.next:
                heappush(min_heap, (node.next.val, index, node.next))
        return pre_head.next
