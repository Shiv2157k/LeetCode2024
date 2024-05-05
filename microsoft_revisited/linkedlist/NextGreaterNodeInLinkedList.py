from typing import Optional, List, Tuple


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def next_larger_nodes(self, head: Optional[ListNode]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        stack: List[Tuple[int, int]] = []
        output: List[int] = []
        ptr = 0

        while head:
            output.append(0)
            while stack and stack[-1][1] < head.val:
                index, _ = stack.pop()
                output[index] = head.val
            stack.append((ptr, head.val))
            ptr += 1
            head = head.next
        return output
