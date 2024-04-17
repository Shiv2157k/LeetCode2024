from typing import List


class InterSectionOfTwoArrays:

    def getIntersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums1:
        :param nums2:
        :return:
        """

        output = []
        seen = {}

        for num1 in nums1:
            seen[num1] = 1

        for num2 in nums2:
            if num2 in seen and seen[num2] == 1:
                output.append(num2)
                seen[num2] = 0
        return output
