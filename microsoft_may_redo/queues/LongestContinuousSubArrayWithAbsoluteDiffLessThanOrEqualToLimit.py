from collections import deque
from typing import List


class ArrayWithAbsoluteDiffLessThanEqualToLimit:

    def longest_subarray(self, nums: List[int], limit: int) -> int:
        """
        Approach: Min and Max Queue
        T: O(N)
        S: O(N)
        :param nums:
        :param limit:
        :return:
        """
        min_queue = deque()
        max_queue = deque()

        left = 0
        right = 0

        while right < len(nums):

            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()

            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()

            max_queue.append(nums[right])
            min_queue.append(nums[right])

            if max_queue[0] - min_queue[0] > limit:

                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                left += 1
            right += 1
        return right - left
