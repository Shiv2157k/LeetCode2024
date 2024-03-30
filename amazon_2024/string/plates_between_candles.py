from typing import List


class PlatesBetweenCandles:

    def numberBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Approach: Cumulative Sum
        T: O(n + q)
        S: O(n + q)
        :param s:
        :param queries:
        :return:
        """
        # left -> right
        candlesToRight = [-1] * len(s)
        # right -> left
        candlesToLeft = [-1] * len(s)
        plates, platesSoFar = [], 0

        for index in range(len(s)):

            # left -> right candle position
            if s[index] == "|":
                candlesToRight[index] = index
            elif index > 0:
                candlesToRight[index] = candlesToRight[index - 1]
            # Cumulative plate until each position
            if s[index] == "*":
                platesSoFar += 1
            plates.append(platesSoFar)

        for index in range(len(s) - 1, -1, -1):
            # left <- right i.e., right -> left
            if s[index] == "|":
                candlesToLeft[index] = index
            elif index < len(s) - 1:
                candlesToLeft[index] = candlesToLeft[index + 1]

        # calculate plates between from the queries
        result = [0] * len(queries)
        for index in range(len(queries)):
            leftCandle = candlesToLeft[queries[index][0]]
            rightCandle = candlesToRight[queries[index][1]]
            
            if leftCandle != -1 and rightCandle != -1 and rightCandle > leftCandle:
                platesBetween = plates[rightCandle] - plates[leftCandle]
                result[index] = platesBetween
        return result


if __name__ == "__main__":
    platesBetweenCandles = PlatesBetweenCandles()

    print(platesBetweenCandles.numberBetweenCandles("**|**|***|", [[2, 5], [5, 9]]))
    print(platesBetweenCandles.numberBetweenCandles("***|**|*****|**||**|*",
                                                    [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
