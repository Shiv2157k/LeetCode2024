from typing import List


class FrequencyOfMostFrequentElements:

    def max_frequency_v1(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left = 0
        right = 0
        curr_sum = 0

        while right < len(nums):
            target = nums[right]
            curr_sum += target

            if (right - left + 1) * target - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            right += 1
        return len(nums) - left

    def max_frequency_v0(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left = 0
        right = 0
        curr_sum = 0
        max_freq = 0

        while right < len(nums):
            target = nums[right]
            curr_sum += target

            while (right - left + 1) * target - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
            right += 1
        return max_freq
