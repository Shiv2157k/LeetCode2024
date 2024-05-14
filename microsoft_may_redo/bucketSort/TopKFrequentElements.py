from typing import List


class TopKFrequentElements:

    def get_top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Bucket Sort
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        top_k = []

        for freq in range(len(bucket) - 1, -1, -1):
            if len(bucket[freq]) != 0:
                curr_bucket = bucket[freq]
                for num in curr_bucket:
                    if len(top_k) == k:
                        return top_k
                    top_k.append(num)
        return top_k
