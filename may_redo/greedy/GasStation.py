from typing import List


class GasStation:


    def con_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param gas:
        :param cost:
        :return:
        """

        total_tank = 0
        curr_tank = 0
        start_circuit = 0

        for i in range(len(gas)):

            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                start_circuit = i + 1
        return start_circuit if total_tank >= 0 else -1