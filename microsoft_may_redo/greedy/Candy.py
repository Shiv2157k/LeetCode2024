from typing import List


class Candy:

    def candy(self, ratings: List[int]) -> int:
        """
        Approach: Peak Valley Single Pass
        T: O(N)
        S: O(1)
        :param ratings:
        :return:
        """

        total_ratings = len(ratings)
        if total_ratings <= 1:
            return total_ratings

        count = lambda n: n * (n + 1) // 2

        up = 0
        down = 0
        old_slope = 0
        min_candies = 0

        for i in range(1, total_ratings):

            new_slope = 0

            # rising slope
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            # falling slope
            elif ratings[i] < ratings[i - 1]:
                new_slope = -1

            # transition state
            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 <= new_slope):
                min_candies += count(up) + count(down) + max(up, down)

                up = 0
                down = 0

            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                min_candies += 1

            old_slope = new_slope

        min_candies += count(up) + count(down) + max(up, down) + 1
        return min_candies

    def min_candies_v1(self, ratings: List[int]) -> int:
        """
        Approach: Greedy with O(N)
        T: O(N)
        S: O(N)
        :param ratings:
        :return:
        """

        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        total_candies = candies[-1]

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total_candies += candies[i]
        return total_candies

    def min_candies_v0(self, ratings: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N^2)
        S: O(N)
        :param ratings:
        :return:
        """

        has_changed = True
        candies = [1] * len(ratings)

        while has_changed:

            has_changed = False

            for i in range(len(ratings)):

                if i != len(ratings) - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] += 1
                    has_changed = True

                if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] += 1
                    has_changed = True
        min_candies = 0
        for candy in candies:
            min_candies += candy
        return min_candies
