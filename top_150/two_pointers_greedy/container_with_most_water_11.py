from typing import List


class Container:

    def withMostWaterArea(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers and GReedy
        T: O(N)
        S: O(1)
        :param heights:
        :return:
        """

        maxArea = 0
        left, right = 0, len(heights) - 1

        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            maxArea = max(maxArea, width * height)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == "__main__":
    container = Container()
    print(container.withMostWaterArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.withMostWaterArea([1, 1]))
