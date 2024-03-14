from typing import List


class Container:

    def with_most_water(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param heights:
        :return:

        # Brute Force:
        T: O(N^2), S: O(1)
        max_area = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                length = min(height[right], height[left])
                max_area = max(max_area, length * width)
        return max_area
        """
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            breadth = right - left
            length = min(heights[left], heights[right])
            max_area = max(max_area, length * breadth)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    container = Container()
    print(container.with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.with_most_water([1, 1]))
