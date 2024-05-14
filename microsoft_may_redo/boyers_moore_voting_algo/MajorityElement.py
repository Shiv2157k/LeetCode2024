from typing import List


class MajorityElement:

    def majority_element(self, nums: List[int]) -> int:
        """
        Approach: Boyers Moore Voting Algorithm
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)
        return candidate
