from typing import List

class ConsecutiveSequence:

    def longest_consecutive_v1(self, nums: List[int]) -> int:
        """
        Approach: Hash Set
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_streak = 1
                while num + 1 in num_set:
                    num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak

    def longest_consecutive_v0(self, nums: List[int]) -> int:
        """
        Approach: Sort
        T: O(N log N)
        S: O(N) -> extra space used during the sort
        :param nums:
        :return:
        """

        if not nums:
            return 0

        nums.sort()
        longest_streak = 0
        curr_streak = 1

        for index in range(1, len(nums)):
            if nums[index - 1] + 1 == nums[index]:
                curr_streak += 1
            else:
                curr_streak = 1
            longest_streak = max(curr_streak, longest_streak)
        return longest_streak


if __name__ == "__main__":
    consecutive_sub_seq = ConsecutiveSequence()
    print(consecutive_sub_seq.longest_consecutive_v0([2, 1, 3, 100, 4, 99]))
    print(consecutive_sub_seq.longest_consecutive_v0([2, 1, 3, 100, 4, 4, 99]))
    print(consecutive_sub_seq.longest_consecutive_v0([1, 1, 1, 1]))
    print(consecutive_sub_seq.longest_consecutive_v0([1, 2, 2, 1]))
    print("**__**")
    print(consecutive_sub_seq.longest_consecutive_v1([2, 1, 3, 100, 4, 99]))
    print(consecutive_sub_seq.longest_consecutive_v1([2, 1, 3, 100, 4, 4, 99]))
    print(consecutive_sub_seq.longest_consecutive_v0([1, 1, 1, 1]))
    print(consecutive_sub_seq.longest_consecutive_v1([1, 2, 2, 1]))