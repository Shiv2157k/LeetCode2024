from typing import List


class ShipPackage:

    def min_capacity_in_d_days(self, weights: List[int], days: int) -> int:
        """
        Approach:
        T: O(N log N)
        S: O(1)
        :param weights:
        :param days:
        :return:
        """

        total_weight = 0
        max_weight = 0
        # our capacity lies in b/w max_weight -- total weight
        # calculate max_weight and total weight
        for weight in weights:
            total_weight += weight
            if max_weight < weight:
                max_weight = weight

        min_capacity, max_capacity = max_weight, total_weight

        # perform a binary search in b/w max_weight <--> total_weight
        # to see if it is feasible
        while min_capacity < max_capacity:
            capacity = min_capacity + (max_capacity - min_capacity) // 2
            # if the current weight is feasible
            # lower the capacity and check
            if self._is_feasible(weights, capacity, days):
                max_capacity = capacity
            # if the current weight is not feasible
            # increase the capacity by 1
            else:
                min_capacity = capacity + 1
        return min_capacity

    def _is_feasible(self, weights: List[int], capacity: int, days: int) -> bool:
        """
        :param weights:
        :param capacity:
        :param days:
        :return:
        """
        # minimum days needed
        days_needed = 1
        # curr weight
        curr_weight = 0
        for weight in weights:
            curr_weight += weight
            # if the curr weight reached the capacity
            # add a day and reset the curr weight
            if curr_weight > capacity:
                days_needed += 1
                curr_weight = weight
        # if it is within days needed it is feasible
        return days_needed <= days


if __name__ == "__main__":
    ship_package = ShipPackage()
    print(ship_package.min_capacity_in_d_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(ship_package.min_capacity_in_d_days([3, 2, 2, 4, 1, 4], 3))
    print(ship_package.min_capacity_in_d_days([1, 2, 3, 1, 1], 4))


