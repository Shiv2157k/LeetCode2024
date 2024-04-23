from collections import deque
from typing import List, Deque


class SlidingWindowMaximum:

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Monotonic Queue
        T: O(N)
        S: O(K)
        :param nums:
        :param k:
        :return:
        """

        queue: Deque[int] = deque()
        result: List[int] = []
        n: int = len(nums)

        # add the elements in first window
        for index in range(k):

            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()

            queue.append(index)

        result.append(nums[queue[0]])

        for index in range(k, n):

            if queue and queue[0] == index - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()

            queue.append(index)
            result.append(nums[queue[0]])
        return result
