from typing import List


class UniqueNumberOfOccurrence:

    def unique_number_of_occurrence(self, arr: List[int]) -> bool:
        """
        Approach: HashMap and HashSet
        T: O(N)
        S: O(N)
        :param arr:
        :return: 
        """

        freq_map = {}

        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        freq_set = set(freq_map.values())
        return len(freq_set) == len(freq_map)
