from typing import List


class RectangleOverlap:

    def is_rectangle_overlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        [x1, y1, x2, y2] -> [x11, y11, x22, y22]
        Approach: Math
        T: O(1)
        S: O(1)
        :param rec1:
        :param rec2:
        :return:
        """
        return not (
                rec1[1] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3]
        )
