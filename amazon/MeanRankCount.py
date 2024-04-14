from typing import List


class MeanRank:



    def getMeanRankCount(self, ranks: List[int]) -> List[int]:

        n = len(ranks)
        result = [0] * n

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += ranks[j]
                mean_rank = total / (j - i + 1)
                if mean_rank.is_integer():
                    result[int(mean_rank) - 1] += 1
        return result


if __name__ == "__main__":
    meanRank = MeanRank()
    print(meanRank.getMeanRankCount([1, 2, 3, 4, 5]))
