from typing import List, Any


class Candies:

    def candy_v3(self, ratings: List[int]) -> int:
        """
        Approach: Peak Valley
        Formula: 1, 2, 3...n => n(n + 1) / 2
        T: O(n)
        S: O(10
        :param ratings:
        :return:
        """

        total_ratings = len(ratings)
        if total_ratings <= 1:
            return total_ratings

        count: Any = lambda n: n * (n + 1) // 2
        candies: int = 0
        up: int = 0
        down: int = 0
        old_slope: int = 0

        for i in range(1, len(ratings)):

            new_slope: int = 0

            # rising slope or peak
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i] < ratings[i - 1]:  # falling slope or valley
                new_slope = -1

            # 1. slope is changing from uphill to flat or downhill
            # 2. slope is changing from downhill to flat or uphill
            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 <= new_slope):
                candies += count(up) + count(down) + max(up, down)

                # reset up and down
                up = 0
                down = 0

            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1
            old_slope = new_slope

        # last count
        candies += count(up) + count(down) + max(up, down)
        return candies

    def candy_v2(self, ratings: List[int]) -> int:
        """
        Approach: One Array
        T: O(N)
        S: O(N)
        :param ratings:
        :return:
        """

        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = 1 + candies[i - 1]

        min_candies = candies[-1]

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(1 + candies[i + 1], candies[i])
            min_candies += candies[i]
        return min_candies

    def candy_v1(self, ratings: List[int]) -> int:
        """
        Approach: Two Array
        T: O(N)
        S: O(N)
        :param ratings:
        :return:
        """

        candies_lr = [1] * len(ratings)
        candies_rl = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies_lr[i] = 1 + candies_lr[i - 1]

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_rl[i] = 1 + candies_rl[i + 1]

        min_candies = 0
        for i in range(len(ratings)):
            min_candies += max(candies_lr[i], candies_rl[i])
        return min_candies

    def candy_v0(self, ratings: List[int]) -> int:
        """
        Approach: Brute Force
        T: O(N^2)
        S: O(N)
        :param ratings:
        :return:
        """
        # validation
        if len(ratings) <= 1:
            return len(ratings)
        # allocate single candy for everyone
        total_ratings = len(ratings)
        candies = [1] * total_ratings

        has_changed = True

        while has_changed:
            has_changed = False

            for i in range(len(ratings)):

                # condition 1: checking right child
                if i != total_ratings - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    has_changed = True

                # condition 2: checking left child
                if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    has_changed = True
        min_candies = 0
        for candy in candies:
            min_candies += candy
        retunr
        min_candies
