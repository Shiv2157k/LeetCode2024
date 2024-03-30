from typing import List


class TwoSumII:

    def getTwoSumIndices(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param numbers:
        :param target:
        :return:
        """

        left, right = 0, len(numbers) - 1

        while left < right:

            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


if __name__ == "__main__":
    twoSumII = TwoSumII()
    print(twoSumII.getTwoSumIndices([1, 3, 6, 9, 10], 9))
    print(twoSumII.getTwoSumIndices([1, 3, 6, 9, 10], 21))
