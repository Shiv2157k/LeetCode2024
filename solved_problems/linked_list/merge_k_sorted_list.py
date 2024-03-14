from typing import Optional, List
from queue import PriorityQueue


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class KSortedLists:

    def merge_v1(self,  lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Merge with Divide and Conquer
        T: O()
        S: O(1)
        :param lists:
        :return:
        """
        k = len(lists)
        interval = 1
        while interval < k:
            for index in range(0, interval + k, interval * 2):
                lists[index] = self.merge_two_sorted_lists(lists[index], lists[index + interval])
            interval *= 2
        return lists[0] if k >= 0 else None

    def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = pointer = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        pointer.next = l1 if l1 else l2
        return pre_head.next

    def merge_v0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Priority Queue
        T: O(N log K)
        S: O(N)
        :param lists:
        :return:
        """
        pre_head = pointer = ListNode(-1)
        pq = PriorityQueue()

        for index, linked_node in enumerate(lists):
            if linked_node:
                pq.put((linked_node.val, index, linked_node))

        while not pq.empty():

            val, index, node = pq.get()
            pointer.next = ListNode(val)
            node = node.next
            pointer = pointer.next
            if node:
                pq.put((node.val, index, node))
        return pre_head.next