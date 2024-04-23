from typing import List


class GasStation:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param gas:
        :param cost:
        :return:
        """

        totalTank: int = 0
        currTank: int = 0
        startPoint: int = 0

        for i in range(len(gas)):

            totalTank += gas[i] - cost[i]
            currTank += gas[i] - cost[i]

            if currTank < 0:
                currTank = 0
                startPoint = i + 1

        if totalTank >= 0:
            return startPoint
        else:
            return -1
