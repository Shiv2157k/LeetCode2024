class DecodeWays:


    def decode_ways_v2(self, s: str) -> int:
        """
        Approach: DP no extra space
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        if s[0] == '0':
            return 0

        length = len(s)
        if length == 1:
            return 1

        second_left = 1
        first_left = 1 if s[1] != '0' else 0

        for i in range(1, length):
            curr = 0
            if s[i] != '0':
                curr += first_left
            two_digit = int(s[i - 1: i + 1])
            if 9 < two_digit <= 26:
                curr += second_left
            second_left, first_left = first_left, curr
        return first_left

    def decode_ways_v1(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        if s[0] == '0':
            return 0

        length = len(s)
        if length == 1:
            return 1

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1 if s[1] != '0' else 0

        for i in range(1, length):

            if s[i] != '0':
                dp[i + 1] += dp[i]

            two_digit = int(s[i - 1: i + 1])
            if 9 < two_digit <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

    def decode_ways_v0(self, s: str) -> int:
        """
        Approach: Recurse with memo
        T: O()
        S: O()
        :param s:
        :return:
        """
        memo = {}

        def helper(ptr: int) -> int:

            if ptr == len(s):
                return 1
            if s[ptr] == '0':
                return 0
            if ptr in memo:
                return memo[ptr]
            if ptr == len(s) - 1:
                return 1

            total_ways = helper(ptr + 1)
            two_digit = int(s[ptr: ptr + 2])
            if 9 < two_digit <= 26:
                total_ways += helper(ptr + 2)
            memo[ptr] = total_ways
            return total_ways

        return helper(0)
