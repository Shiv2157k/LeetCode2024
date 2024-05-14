from typing import Optional, List
from heapq import heappop, heappush
from queue import PriorityQueue


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class MergeKSortedList:

    def merge_k_sorted_list(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Merge with Divide and Conquer
        T: O(N log K)
        S: O(N)
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
                lists[i] = self.__merge_two_sorted_list(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def __merge_two_sorted_list(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

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

    def merge_k_sorted_list_v01(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Min Heap or  PQ
        T: O(N log K)
        S: O(N)
        :param lists:
        :return:
        """
        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        pre_head = ListNode(-1)
        prev = pre_head

        min_heap = []

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

    def merge_k_sorted_list_v0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Min Heap or  PQ
        T: O(N log K)
        S: O(N)
        :param lists:
        :return:
        """
        if not lists or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        pre_head = ListNode(-1)
        prev = pre_head

        pq = PriorityQueue()

        for index, linked_list in enumerate(lists):
            if linked_list:
                pq.put((linked_list.val, index, linked_list))

        while not pq.empty():

            val, index, node = pq.get()
            prev.next = ListNode(val)
            prev = prev.next
            if node.next:
                pq.put((node.next.val, index, node.next))
        return pre_head.next
