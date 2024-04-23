from typing import List


class MostFrequentElements:

    def maxFrequencyV1(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window Advanced
        T: O(N log N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left, right = 0, 0
        curr = 0

        while right < len(nums):

            curr += nums[right]
            target = nums[right]

            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
        return len(nums) - left

    def maxFrequencyV0(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N log N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        nums.sort()
        left, right = 0, 0
        curr = 0
        maxFreq = 0

        while right < len(nums):

            curr += nums[right]
            target = nums[right]

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)
            right += 1
        return maxFreq
