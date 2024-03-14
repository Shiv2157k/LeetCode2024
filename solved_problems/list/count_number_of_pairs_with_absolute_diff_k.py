import collections
from typing import List

class UnSortedList:

    def count_number_of_pairs_with_absolute_diff_k(self, nums: List[int], k: int) -> int:
        """
        Approach: HashMap Counter
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """
        num_occurrence = collections.Counter()
        map = collections.defaultdict(int)
        total_pairs = 0

        for num in nums:
            total_pairs += map[num + k] + map[num - k]
            map[num] += 1
        return total_pairs


if __name__ == "__main__":
    unsortedList = UnSortedList()
    print(unsortedList.count_number_of_pairs_with_absolute_diff_k(
        [1, 2, 2, 1], 1
    ))
    print(unsortedList.count_number_of_pairs_with_absolute_diff_k(
        [3, 2, 1, 5, 4], 2
    ))
    print(unsortedList.count_number_of_pairs_with_absolute_diff_k(
        [1, 3], 3
    ))

