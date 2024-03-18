from typing import List
from enum import Enum, auto


class Index:
    GOOD = auto()
    BAD = auto()
    UNKNOWN = auto()


class JumpGame:

    def reached_destination_v3(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        max_reach = 0
        for index in range(len(nums)):
            if max_reach < index + nums[index]:
                max_reach = index + nums[index]
            if max_reach == index:  # game over lost
                break
        return max_reach >= len(nums) - 1

    def reached_destination_v4(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        destination = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= destination:
                destination = index
        return destination == 0

    def reached_destination_v2(self, nums: List[int]) -> bool:
        """
        Approach: DP (Bottom Up Approach)
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        dp = [Index.UNKNOWN] * length
        dp[-1] = Index.GOOD

        for right in range(length - 2, -1, -1):
            curr_jump = min(nums[right] + right, length - 1)
            for index in range(right + 1, curr_jump + 1):
                if dp[index] == Index.GOOD:
                    dp[right] = Index.GOOD
        return dp[0] == Index.GOOD

    def reached_destination_v1(self, nums: List[int]) -> bool:
        """
        Approach: Recursion with Memoization (TopDown Approach)
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        memo = [Index.UNKNOWN] * length
        # last index is good and it can reach the destination itself.
        memo[-1] = Index.GOOD

        def can_jump_to_curr_position(position: int) -> bool:
            # base case
            if memo[position] != Index.UNKNOWN:
                return memo[position] == Index.GOOD

            curr_jump = min(position + nums[position], length - 1)
            for curr_index in range(position + 1, curr_jump + 1):
                if can_jump_to_curr_position(curr_index):
                    memo[position] = Index.GOOD
                    return True
            memo[position] = False
            return False
        return can_jump_to_curr_position(0)

    def reached_destination_v0(self, nums: List[int]) -> bool:
        """
        Approach: Recursion
        T: O(N^3)
        S: O()
        :param nums:
        :return:
        """
        length = len(nums)

        def can_jump_to_position(position: int) -> bool:
            # base case
            if position == length - 1:
                return True  # we reached destination

            curr_jump = min(position + nums[position], length - 1)
            # iterate over to next possibilities
            for curr_index in range(position + 1, curr_jump + 1):
                if can_jump_to_position(curr_index):
                    return True
            return False

        return can_jump_to_position(0)


if __name__ == "__main__":
    game = JumpGame()
    print("**_|_**")
    print(game.reached_destination_v0([2, 3, 1, 1, 4]))
    print(game.reached_destination_v0([2, 2, 1, 0, 4]))
    print("**_|_**")
    print(game.reached_destination_v1([2, 3, 1, 1, 4]))
    print(game.reached_destination_v1([2, 2, 1, 0, 4]))
    print("**_|_**")
    print(game.reached_destination_v2([2, 3, 1, 1, 4]))
    print(game.reached_destination_v2([2, 2, 1, 0, 4]))
    print("**_|_**")
    print(game.reached_destination_v3([2, 3, 1, 1, 4]))
    print(game.reached_destination_v3([2, 2, 1, 0, 4]))
    print("**_|_**")
