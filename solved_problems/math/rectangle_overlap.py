from typing import List


class Rectangle:

    def is_overlap(self, r1: List[int], r2: List[int]) -> bool:
        """
        Approach: Negation of not overlap
        left, right, top, bottom
        S: O(1)
        :param r1:
        :param r2:
        :return:
        """
        # straight line -> negative overlap
        if r1[0] == r1[2] or r1[1] == r1[3] or r2[0] == r2[2] or r2[1] == r2[3]:
            return False

        return not (
                r1[2] <= r2[0] or  # left
                r1[3] <= r2[1] or  # bottom
                r1[0] >= r2[2] or  # right
                r2[1] >= r2[3]  # top
        )
