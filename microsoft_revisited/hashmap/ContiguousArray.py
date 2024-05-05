from typing import List, Dict


class ContiguousArray:

    def find_max_length(self, nums: List[int]) -> int:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        count_index_map: Dict[int, int] = {0: -1}

        max_len: int = 0
        count: int = 0

        for i in range(len(nums)):
            count = count + (1 if nums[i] == 1 else -1)

            if count in count_index_map:
                max_len = max(max_len, i - count_index_map[count])
            else:
                count_index_map[count] = i
        return max_len