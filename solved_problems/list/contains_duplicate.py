from typing import List


class ArrayList:

    def contains_duplicate(self, nums: List[int]):
        """
        Approach: Hash Table
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            if freq_map[num] > 1:
                return True
        return False


if __name__ == "__main__":
    arr = ArrayList()
    print(arr.contains_duplicate([1, 2, 3, 1]))
    print(arr.contains_duplicate([9, 7, 8, 5]))
