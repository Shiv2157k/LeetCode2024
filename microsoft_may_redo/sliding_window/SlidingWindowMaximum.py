from collections import deque
from typing import List


class SlidingWindowMaximum:

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Double ended queue / Monotonic Deque
        T: O(N)
        S: O(K)
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        queue = deque()
        result = []

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        result.append(nums[queue[0]])

        for i in range(k, n):
            # check window size
            if queue and queue[0] == i - k:
                queue.popleft()
            # check max number
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
        return result
