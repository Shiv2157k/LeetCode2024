from typing import Optional


class LinkedNode:

    def __init__(self, val:int=-1, next=None):
        self.val = val
        self.next =next


class LinkedList:

    def reverse_v1(self, head: Optional[LinkedNode]) -> Optional[LinkedNode]:
        """
        Approach: Iterative
        T: O(N)
        S:O(1)
        :param head:
        :return:
        """

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverse_v0(self, head: Optional[LinkedNode]) -> Optional[LinkedNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        # base case
        if not head or not head.next:
            return head

        # if input is  1->2->3->4->5
        # our head would like below now
        # head = 5->4->3->2<-1
        # need to fix (2<-1) part
        node = self.reverse_v0(head.next)

        head.next.next = head
        head.next = None
        return node


if __name__ == "__main__":

    l1 = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5)))))

    linked_list = LinkedList()
    l2 = linked_list.reverse_v1(l1)
    l3 = l2

    while l3:
        print(l3.val, end="->")
        l3 = l3.next

    l5 = linked_list.reverse_v0(l1)
    l4 = l5

    while l4:
        print(l4.val, end="->")
        l4 = l4.next