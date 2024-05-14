class ClimbingStairs:

    def total_ways(self, n: int) -> int:
        """
        Approach: Greedy or DP with no extra space
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """
        if n <= 2:
            return n

        prev_step = 1
        curr_step = 2

        for i in range(3, n + 1):
            next_step = prev_step + curr_step
            prev_step, curr_step = curr_step, next_step
        return curr_step
