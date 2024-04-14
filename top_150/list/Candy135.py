from typing import List


class Candy:

    def minimumDistributionV2(self, ratings: List[int]):
        """
        Approach: Single Pass Peak and Valley
        T: O(N)
        S: O(1)
        :param ratings:
        :return:
        """

        totalRatings = len(ratings)
        if totalRatings <= 1:
            return totalRatings

        calculateCount = lambda n: n * (n + 1) // 2

        candies = 0
        up, down = 0, 0
        oldSlope = 0

        for i in range(1, totalRatings):

            newSlope = 0
            if ratings[i] > ratings[i - 1]:
                newSlope = 1
            elif ratings[i] < ratings[i - 1]:
                newSlope = -1

            if (oldSlope > 0 and newSlope == 0) or (oldSlope < 0 <= newSlope):

                candies += calculateCount(up) + calculateCount(down) + max(up, down)
                # reset
                up = 0
                down = 0

            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1
            oldSlope = newSlope

        candies += calculateCount(up) + calculateCount(down) + max(up, down) + 1
        return candies


    def minimumDistributionV1(self, ratings: List[int]):
        """
        Approach: Single Array
        T: O(N)
        S: O(N)
        :param ratings:
        :return:
        """
        totalRatings = len(ratings)
        if totalRatings <= 1:
            return totalRatings

        candies = [1] * totalRatings

        for i in range(1, totalRatings):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        totalCandies = candies[-1]
        for i in range(totalRatings - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            totalCandies += candies[i]
        return totalCandies

    def minimumDistributionV0(self, ratings: List[int]):
        """
        You are giving candies to these children subjected to the following requirements:
        - Each child must have at least one candy.
        - Children with a higher rating get more candies than their neighbors.
        Approach: Two Arrays
        T: O(N)
        S: O(N)
        :param ratings:
        :return:
        """

        totalRatings = len(ratings)
        if totalRatings <= 1:
            return totalRatings

        leftToRight = [1] * totalRatings
        rightToLeft = [1] * totalRatings
        totalCandies = 0

        for i in range(1, totalRatings):
            if ratings[i] > ratings[i - 1]:
                leftToRight[i] = leftToRight[i - 1] + 1

        for i in range(totalRatings - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rightToLeft[i] = rightToLeft[i + 1] + 1

        for i in range(totalRatings):
            totalCandies += max(leftToRight[i], rightToLeft[i])

        return totalCandies


if __name__ == "__main__":
    candy = Candy()
    print(candy.minimumDistributionV0([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))
    print(candy.minimumDistributionV1([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))
    print(candy.minimumDistributionV2([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))

