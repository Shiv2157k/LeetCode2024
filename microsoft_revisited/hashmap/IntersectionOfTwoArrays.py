from typing import List, Dict


class TwoArrays:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param nums1:
        :param nums2:
        :return:
        """

        lookup: Dict[int, int] = {}
        intersection_elements: List[int] = []

        for num1 in nums1:
            lookup[num1] = 1

        for num2 in nums2:

            if num2 in lookup and lookup[num2] == 1:
                intersection_elements.append(num2)
                lookup[num2] = 0
        return intersection_elements
