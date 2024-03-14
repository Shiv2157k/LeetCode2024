from typing import List


class Solution:

    def twoSum__(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Brute Force
        :param nums:
        :param target:
        :return:
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSum_(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Two Pass
        :param nums:
        :param target:
        :return:
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement], i]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Single Pass
        :param nums:
        :param target:
        :return:
        """
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i


if __name__ == "__main__":
    twoSum = Solution()
    print(twoSum.twoSum__([2, 5, 3, 4], 8))
    print(twoSum.twoSum__([2, 5], 7))
    print(twoSum.twoSum_([2, 5, 3, 4], 8))
    print(twoSum.twoSum_([2, 5], 7))
    print(twoSum.twoSum([2, 5, 3, 4], 8))
    print(twoSum.twoSum([2, 5], 7))
