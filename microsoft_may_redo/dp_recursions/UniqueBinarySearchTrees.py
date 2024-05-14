class BinaryTree:

    def unique_binary_search_trees(self, n: int) -> int:
        """
        Approach: Dp
        T: O(N^2)
        S: O(N)
        :param n:
        :return:
        """

        dp = [0] * (n + 1)
        # 0, 1, 2....n
        # i - 1: i - j
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
