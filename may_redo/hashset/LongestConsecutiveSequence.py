from typing import Set, List


class ConsecutiveSequence:

    def longest(self, nums: List[int]) -> int:
        """
        Approach: Set
        T: O(N)
        S: O(N)
        :param nums:
        :return: 
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:

            if num - 1 not in num_set:

                curr_streak = 1
                curr_num = num
                while curr_num + 1 in num_set:
                    curr_streak += 1
                    curr_num += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
