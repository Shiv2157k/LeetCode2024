class WaterBottlesII:

    def max_bottles_drunk(self, num_bottles: int, num_exchange: int) -> int:
        """
        Approach: Math
        T: O(N)
        S: O(1)
        :param num_bottles:
        :param num_exchange:
        :return:
        """

        total_bottles = num_bottles

        while num_bottles >= num_exchange:
            num_bottles -= (num_exchange - 1)
            total_bottles += 1
            num_exchange += 1
        return total_bottles
