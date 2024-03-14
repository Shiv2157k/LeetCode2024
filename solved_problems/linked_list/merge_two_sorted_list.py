class ListNodes:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_two_sorted_list_(self, l1: ListNodes, l2: ListNodes) -> ListNodes:
        """
        Approach: Recursion
        T: O(M + N)
        S: O(M + N)
        :param l1:
        :param l2:
        :return:
        """
        if not l2:
            return l1
        elif not l1:
            return l2
        elif l1.val < l2.val:
            l1.next = self.merge_two_sorted_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_sorted_list(l1, l2.next)
            return l2

    def merge_two_sorted_list(self, l1: ListNodes, l2: ListNodes):
        """
        T: O(M + N)
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """
        # base case/ validation
        if not l1:
            return l2
        if not l2:
            return l1
        prehead = ListNodes(-1)
        # iterator
        prev = prehead

        # while there are nodes in the two linked list
        while l1 and l2:
            if l1.val <= l2.val:
                # route prev.next to l1
                prev.next = l1
                # move to the next l1 node
                l1 = l1.next
            else:
                # route prev.next to l1
                prev.next = l2
                # move to next l2 node
                l2 = l2.next
            # keep moving the iterator to next for linking the node
            prev = prev.next
        # if any of the l1 and l2 node exists set the link to prev
        prev.next = l1 if l1 is not None else l2
        # prev is the after the prehead
        return prehead.next


if __name__ == "__main__":
    l1 = ListNodes(1)
    l1.next = ListNodes(3)
    l1.next.next = ListNodes(5)

    l2 = ListNodes(1)
    l2.next = ListNodes(2)
    l2.next.next = ListNodes(4)

    linkedList = LinkedList()
    output = linkedList.merge_two_sorted_list(l1, l2)
    while output:
        print(output.val)
        output = output.next
