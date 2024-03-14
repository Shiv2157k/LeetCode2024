from typing import List


class GasStation:

    def find_start_point(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param gas:
        :param cost:
        :return:
        """
        total_tank = current_tank = starting_point = 0
        for i, fuel in enumerate(gas):
            total_tank += fuel - cost[i]
            current_tank += fuel - cost[i]
            if current_tank < 0:
                starting_point += 1
                current_tank = 0
        return starting_point if total_tank >= 0 else -1


if __name__ == "__main__":
    gas_station = GasStation()
    print(gas_station.find_start_point(
        [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    ))
    print(gas_station.find_start_point(
        [2, 3, 4], [3, 4, 3]
    ))
