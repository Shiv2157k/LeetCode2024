from typing import List


class ConsecutiveSequence:

    def longestV0(self, nums: List[int]) -> int:
        """
        Approach: Sort
        T: O(N log N)
        S: O(1)
        :param nums:
        :return:
        """
        if not nums:
            return 0

        nums.sort()
        longestStreak = 1
        currStreak = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                if nums[index] == nums[index - 1] + 1:
                    currStreak += 1
                else:
                    longestStreak = max(currStreak, longestStreak)
                    currStreak = 1
        return max(longestStreak, currStreak)

    def longestV1(self, nums: List[int]) -> int:
        """
        Approach: Hash Set
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        numSet = set(nums)
        longestStreak = 1

        for num in numSet:

            if num - 1 not in numSet:
                currNum = num
                currStreak = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currStreak += 1

                if currStreak >= longestStreak:
                    longestStreak = currStreak
        return longestStreak


if __name__ == "__main__":
    consecutiveSequence = ConsecutiveSequence()
    print(consecutiveSequence.longestV1([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(consecutiveSequence.longestV0([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
