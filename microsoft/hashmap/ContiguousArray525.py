from typing import List


class ContiguousArray:

    def findMaxLength(self, nums: List[int]):
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        countIndexMap = {0: -1}

        maxLen, count = 0, 0

        for i in range(len(nums)):
            count += (1 if nums[i] == 1 else -1)
            if count in countIndexMap:
                maxLen = max(maxLen, i - countIndexMap[count])
            else:
                countIndexMap[count] = i
        return maxLen


if __name__ == "__main__":
    contiguousArray = ContiguousArray()
    print(contiguousArray.findMaxLength([0, 1, 0, 0, 1, 1, 0]))
