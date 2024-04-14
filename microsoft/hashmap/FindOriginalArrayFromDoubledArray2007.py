from typing import List


class OriginalToDoubledArray:

    def findOriginalArrayV1(self, changed: List[int]) -> List[int]:
        """
        Approach: Counting Sort
        T: O(N + K)
        S: O(K)
        :param changed:
        :return:
        """

        maxNum = 0
        for num in changed:
            maxNum = max(maxNum, num)

        freqBucket = [0] * (maxNum * 2)

        for num in changed:
            freqBucket[num] += 1

        original = []
        num = 0
        while num <= maxNum:

            if freqBucket[num] > 0:
                freqBucket[num] -= 1
                if freqBucket[num * 2] > 0:
                    freqBucket[num * 2] -= 1
                    original.append(num)
                    num -= 1
                else:
                    return []
            num += 1
        return original

    def findOriginalArrayV0(self, changed: List[int]) -> List[int]:
        """
        Approach: HashMap
        T: O(N log N)
        S: O(N)
        :param changed:
        :return:
        """

        # validation
        if len(changed) % 2 == 1:
            return []

        changed.sort()
        freqMap = {}

        for num in changed:
            freqMap[num] = freqMap.get(num, 0) + 1

        original = []
        for num in changed:

            if freqMap[num] > 0:
                freqMap[num] -= 1
                twiceNum = num * 2
                if twiceNum in freqMap and freqMap[twiceNum] > 0:
                    freqMap[twiceNum] -= 1
                    original.append(num)
                else:
                    return []
        return original
