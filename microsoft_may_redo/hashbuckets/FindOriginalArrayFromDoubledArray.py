from typing import List


class DoubledArray:

    def find_original_array(self, changed: List[int]) -> List[int]:
        """
        Approach: Freq Hash Bucket
        T: O(N + K)
        S: O(K)
        :param changed:
        :return:
        """

        max_num = 0

        for num in changed:
            if max_num < num:
                max_num = num

        freq_bucket = [0] * ((max_num * 2) + 1)

        for num in changed:
            freq_bucket[num] += 1

        original = []
        num = 0

        while num <= max_num:

            if freq_bucket[num] > 0:
                freq_bucket[num] -= 1

                if freq_bucket[num * 2] > 0:
                    freq_bucket[num * 2] -= 1
                    original.append(num)
                    num -= 1
                else:
                    return []
            num += 1
        return original
