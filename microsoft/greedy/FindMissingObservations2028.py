from typing import List


class DiceRolls:

    def findMissingObservations(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Approach: Greedy
        T: O(N)
        S: O(N)
        :param rolls:
        :param mean:
        :param n:
        :return:
        """
        # number of times dice rolled
        m = len(rolls)
        rolled = 0

        # calculate total rolled count
        for roll in rolls:
            rolled += roll

        # total that needs to be rolled
        nTotal = (mean * (m + n)) - rolled

        # base case/ validation
        if nTotal < n or nTotal > n * 6:
            return []

        res = []
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            res.append(dice)
            nTotal -= dice
            n -= 1
        return res


if __name__ == "__main__":
    diceRolls = DiceRolls()
    print(diceRolls.findMissingObservations([3, 2, 4, 3], 4, 2))
    print(diceRolls.findMissingObservations([2, 2, 2, 2], 2, 2))
    print(diceRolls.findMissingObservations([1, 5, 6], 3, 4))
