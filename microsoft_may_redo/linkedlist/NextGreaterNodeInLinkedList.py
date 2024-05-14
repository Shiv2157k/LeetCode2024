from typing import Optional, List


class ListNode:

    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def next_greater_node(self, head: Optional[ListNode]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        stack = []
        pointer = head
        output = []

        ptr = 0
        while pointer:
            output.append(0)
            while stack and stack[-1][1] < pointer.val:
                curr_id, _ = stack.pop()
                output[curr_id] = pointer.val

            stack.append((ptr, pointer.val))
            ptr += 1
            pointer = pointer.next
        return output
