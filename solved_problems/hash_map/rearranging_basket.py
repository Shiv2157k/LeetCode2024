from typing import List


class FruitBaskets:

    def re_arrange_with_min_cost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Approach: HashMap and Greedy Pick
        T: O(N log N)
        S: O(N)
        :param basket1:
        :param basket2:
        :return:
        """
        # for collecting frequency
        cost_swap_freq = {}

        for fruit_cost in basket1:
            cost_swap_freq[fruit_cost] = cost_swap_freq.get(fruit_cost, 0) + 1

        # decrement the freq with basket2 fruit costs so that we know what costs requires swapping
        for fruit_cost in basket2:
            cost_swap_freq[fruit_cost] = cost_swap_freq.get(fruit_cost, 0) - 1

        # this contains costs that need to swap from both the baskets
        cost_swap_arr = []

        # iterate over the hashmap
        for fruit_cost, frequencies in cost_swap_freq.items():
            # if the frequencies are odd, impossible to balance the baskets cost
            if frequencies % 2 != 0:
                return - 1

            cost_swap_arr += [fruit_cost] * abs(frequencies // 2)

        # pick the min value from both baskets to perform 2 transition level swap
        min_cost = min(basket1 + basket2)

        # sort the cost_swap arr to pick the left min elements as that is all we needed for min cost swap
        # we can optimize using quick select algorithm to be made this to O(N) from O(N log N)
        cost_swap_arr.sort()
        total_min_cost = 0

        # loop through the cost_swap until its pivot index
        # as we swap two elements at a time traversing until mid should be enough
        for cost in range(0, len(cost_swap_arr) // 2):
            # we have to cases to pick the min cost
            # case1: 2 * min_cost in the basket
            # case2: the actual cost we are swapping itself
            # we greedily choose case 1 or case 2 depending on which one gives min cost
            total_min_cost += min((2 * min_cost), cost_swap_arr[cost])
        return total_min_cost


if __name__ == "__main__":
    fruit_baskets = FruitBaskets()
    print(fruit_baskets.re_arrange_with_min_cost(
        [2, 2, 3, 3, 3, 3, 4, 4, 5],
        [5, 5, 3, 3, 2, 2, 6, 6, 5]
    ))
    print(fruit_baskets.re_arrange_with_min_cost(
        [1, 2, 2, 3, 3, 3, 3, 4, 4, 5],
        [5, 5, 3, 3, 2, 2, 6, 6, 5, 1]
    ))
    print(fruit_baskets.re_arrange_with_min_cost(
        [2, 3, 4, 1],
        [3, 2, 5, 1]
    ))
