from typing import List


class MajorityElement:


    def majorityElementV1(self, nums: List[int]) -> int:
        """
        Approach: Boyer-Moore Voting Algorithm
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate

    def majorityElementV0(self, nums: List[int]) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        freqMap = {}
        maxFreq = 0
        candidate = nums[0]
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

            if maxFreq < freqMap[num]:
                maxFreq = freqMap[num]
                candidate = num
        return candidate