from typing import List


class ContiguousArray:

    def find_max_length(self, nums: List[int]) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        max_len = 0
        # this map tracks the start index point of the count seen
        # sentinel for edge case
        count_index_map = {0: -1}
        count = 0

        for index, num in enumerate(nums):
            count += 1 if nums[index] == 1 else -1
            if count in count_index_map:
                max_len = max(max_len, index - count_index_map[count])
            else:
                count_index_map[count] = index
        return max_len
