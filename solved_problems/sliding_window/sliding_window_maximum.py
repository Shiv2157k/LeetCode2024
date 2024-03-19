from collections import deque
from typing import List


class SlidingWindow:

    def find_max_in_k_window(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Monotonic Deque
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        length = len(nums)
        queue = deque()
        max_results = []

        for index in range(k):
            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()
            queue.append(index)

        max_results.append(nums[queue[0]])

        for index in range(k, length):

            if queue and index - k == queue[0]:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()
            queue.append(index)
            max_results.append(nums[queue[0]])
        return max_results


if __name__ == "__main__":
    sliding_window = SlidingWindow()
    print(sliding_window.find_max_in_k_window([1, 3, -1, -3, 5, 3], 3))