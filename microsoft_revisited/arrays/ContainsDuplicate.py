from typing import List


class ContainDuplicates:

    def contains(self, nums: List[int]) -> bool:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
