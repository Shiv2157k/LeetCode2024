from typing import List


class FrequencyOfMostFrequentElement:

    def max_frequency_v1(self, nums: List[int], k: int) -> int:
        """
        Approach: Sort + Sliding Window Optimized
        T: O(N log N)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left: int = 0
        right: int = 0
        curr = 0

        while right < len(nums):
            target = nums[right]
            curr += target

            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            right += 1
        return len(nums) - left

    def max_frequency_v0(self, nums: List[int], k: int) -> int:
        """
        Approach: Sort + Sliding Window
        T: O(N log N)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left: int = 0
        right: int = 0
        max_freq: int = 0
        curr = 0

        while right < len(nums):

            target = nums[right]
            curr += target

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
            right += 1
        return max_freq