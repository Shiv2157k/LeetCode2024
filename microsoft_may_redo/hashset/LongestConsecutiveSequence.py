from typing import List


class LongestConsecutiveSequence:


    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_streak = 1
                curr_num = num

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                if curr_streak > longest_streak:
                    longest_streak = curr_streak
        return longest_streak
