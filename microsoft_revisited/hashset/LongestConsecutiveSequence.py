from typing import List


class LongestConsecutiveSequence:

    def longestConsecutiveSeq(self, nums: List[int]) -> int:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        longestStreak = 0
        numSet = set(nums)

        for num in numSet:

            if num - 1 not in numSet:
                currNum = num
                currStreak = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currStreak += 1
                longestStreak = max(longestStreak, currStreak)
        return longestStreak
