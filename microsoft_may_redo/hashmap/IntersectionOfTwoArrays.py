from typing import List


class IntersectionOfTwoArrays:

    def intersection(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Approach: Hash Map
        T: O(N + M)
        S: O(N)
        :param nums1:
        :param nums2:
        :return:
        """

        output = []
        seen = {}

        for num in nums1:
            seen[num] = 1

        for num in nums2:

            if num in seen and seen[num] == 1:
                output.append(num)
                seen[num] = 0
        return output
