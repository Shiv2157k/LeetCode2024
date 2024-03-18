from typing import List


class JumpGameII:

    def min_jumps_v0(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        dp = [0] * n
        left = 0
        for right in range(1, n):
            while left + nums[left] < right:
                left += 1
            dp[right] = dp[left] + 1
        return dp[-1]

    def min_jumps_v1(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        curr_end = curr_far = 0
        min_jumps, length = 0, len(nums)

        for index in range(length - 1):
            curr_far = max(curr_far, nums[index] + index)

            if curr_end == index:
                min_jumps += 1
                curr_end = curr_far
        return min_jumps


if __name__ == "__main__":
    jump_game_ii = JumpGameII()
    print(jump_game_ii.min_jumps([2, 3, 1, 0, 2, 2, 3]))
