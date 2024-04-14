from typing import List


class GasStation:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy One Pass
        T: O(N)
        S: O(1)
        :param gas:
        :param cost:
        :return:
        """

        totalTank = currTank = startPoint = 0

        for i, fuel in enumerate(gas):

            totalTank += fuel - cost[i]
            currTank += fuel - cost[i]

            if currTank > 0:
                currTank = 0
                startPoint = i + 1
        return startPoint if totalTank >= 0 else -1

