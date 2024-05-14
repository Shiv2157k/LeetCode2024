from typing import List
from heapq import heappop, heappush
from math import inf


class Workers:

    def min_cost_to_hire_k_workers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Approach: Max Heap
        T: O(N log N + N log K)
        S: O(N + k)
        :param quality:
        :param wage:
        :param k:
        :return:
        """

        n = len(quality)
        current_total_quality = 0
        wage_to_quality_ratio = []
        total_cost = inf

        # 1: Calculate the wage to quality ratio and store with quality
        # Wage to quality ratio of an individual = wage / quality
        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        # sort them as we want the min cost
        wage_to_quality_ratio.sort(key=lambda x: x[0])

        highest_quality_workers = []  # this will be our max heap

        # to determine optimal worker pool
        # (max_quality / unit) * total_quality(k)
        for i in range(n):
            heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            # append this to current total quantity
            current_total_quality += wage_to_quality_ratio[i][1]

            # check if we are within k range if not pop
            if len(highest_quality_workers) > k:
                # decrement the current t
                # + as it is negative in the heap
                current_total_quality += heappop(highest_quality_workers)

            # if we are with in range calculate min cost according to our rules
            if len(highest_quality_workers) == k:
                total_cost = min(total_cost, current_total_quality * wage_to_quality_ratio[i][0])
        return total_cost
