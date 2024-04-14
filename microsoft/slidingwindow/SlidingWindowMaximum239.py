from collections import deque
from typing import List


class SlidingWindow:


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Queue
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        queue = deque()
        result = []

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        result.append(nums[queue[0]])

        for i in range(k, len(nums)):

            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
        return result