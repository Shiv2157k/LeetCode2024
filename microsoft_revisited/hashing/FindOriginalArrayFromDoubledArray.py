from typing import List


class DoubleArray:

    def find_original_array(self, changed: List[int]) -> List[int]:
        """
        Approach: Freq Bucket
        T: O(N + K)
        S: O(K)
        :param changed:
        :return:
        """

        max_num: int = 0
        for num in changed:
            if max_num < num:
                max_num = num

        freq_bucket = [0] * ((max_num * 2) + 1)
        for num in changed:
            freq_bucket[num] += 1

        original: List[int] = []
        num = 0

        while num <= max_num:

            if freq_bucket[num] > 0:
                freq_bucket[num] -= 1
                if freq_bucket[num * 2] > 0:
                    freq_bucket[num * 2] -= 1
                    original.append(num)
                    # reset to see if there is similar number and its double.
                    num -= 1
                else:
                    return []
            num += 1
        return original
