from collections import deque
from typing import List


class LongestSubArrWithAbsDiffLEqToLimit:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Approach: Caterpillar method with two monotonic queues
        T: O(N)
        S: O(N)
        :param nums:
        :param limit:
        :return:
        """

        minQueue, maxQueue = deque(), deque()
        left, right = 0, 0

        while right < len(nums):

            while maxQueue and nums[right] > maxQueue[-1]:
                maxQueue.pop()
            while minQueue and nums[right] < minQueue[-1]:
                minQueue.pop()

            minQueue.append(nums[right])
            maxQueue.append(nums[right])

            if maxQueue[0] - minQueue[0] > limit:

                if minQueue[0] == nums[left]:
                    minQueue.popleft()
                if maxQueue[0] == nums[left]:
                    maxQueue.popleft()
                left += 1
            right += 1
        return right - left

