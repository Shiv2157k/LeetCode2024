from typing import List
from collections import defaultdict


class PairOfSongs:

    def total_duration_divisible_by_60_v1(self, time: List[int]) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param time:
        :return:
        """
        # remainder_freq = {i:0 for i in range(61)}
        remainder_freq = defaultdict(int)
        result = 0

        for duration in time:
            # a % 60 == 0 and b % 60 == 0
            if duration % 60 == 0:
                result += remainder_freq[0]
            else:  # a % 60 + b % 60 = 60
                result += remainder_freq[60 - duration % 60]
            remainder_freq[duration % 60] += 1
        return result

    def total_duration_divisible_by_60(self, time: List[int]) -> int:
        """
        Approach: Brute Force
        T: O(N^2)
        S: O(1)
        :param time:
        :return:
        """

        count = 0

        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count


if __name__ == "__main__":
    song_pairs = PairOfSongs()
    print(song_pairs.total_duration_divisible_by_60([30, 20, 150, 100, 40]))
    print(song_pairs.total_duration_divisible_by_60([60, 30, 20, 150, 120, 100, 30]))
    print(song_pairs.total_duration_divisible_by_60_v1([30, 20, 150, 100, 40]))
    print(song_pairs.total_duration_divisible_by_60_v1([60, 30, 20, 150, 120, 100, 30]))
