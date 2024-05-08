class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def delete_node(self, node: ListNode):
        """
        Approach: Overwrite
        T: O(1)
        S: O(1)
        :param node:
        :return:
        """

        node.val = node.next.val
        node.next = node.next.next
