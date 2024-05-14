class DecodeWays:

    def num_ways_v2(self, s: str) -> int:
        """
        Approach: DP with no extra space
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        second_left = 1
        first_left = 1 if s[1] != '0' else 0

        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current += first_left
            two_digit = int(s[i - 1: i + 1])
            if 9 < two_digit <= 26:
                current += second_left
            second_left, first_left = first_left, current
        return first_left

    def num_ways_v1(self, s: str) -> int:
        """
        Approach: DP Tabulation
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1 if s[1] != '0' else 0

        for i in range(1, length):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            two_digits = int(s[i - 1: i + 1])
            if 9 < two_digits <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

    def num_ways_v0(self, s: str) -> int:
        """
        Approach: Recurse with memo
        T: O()
        S: O()
        :param s:
        :return:
        """

        def helper(pos: int):

            if pos == len(s):
                return 1
            if s[pos] == '0':
                return 0
            if pos in memo:
                return memo[pos]
            if pos == len(s) - 1:
                return 1

            total_ways = helper(pos + 1)

            two_digits = s[pos: pos + 2]
            if 9 < int(two_digits) <= 26:
                total_ways += helper(pos + 2)
            memo[pos] = total_ways
            return total_ways

        memo = {}
        return helper(0)
