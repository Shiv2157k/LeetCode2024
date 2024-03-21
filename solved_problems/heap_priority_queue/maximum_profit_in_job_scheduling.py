from heapq import heappop, heappush
from typing import List


class JobScheduling:

    # ToDo: DP -> need to do binary search to find the valid next start time
    # consider or not consider next job

    def max_profit(self, start_times: List[int], end_times: List[int], profits: List[int]) -> int:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N)
        :param start_time:
        :param end_time:
        :param profits:
        :return:
        """

        jobs = []
        for start_time, end_time, profit in zip(start_times, end_times, profits):
            jobs.append((start_time, end_time, profit))

        jobs.sort(key=lambda x: x[0])
        min_heap = []
        max_profit = curr_profit = 0

        for start_time, end_time, profit in jobs:

            # if the previous end time less than equal to next start time
            # pick compare current profit
            while min_heap and min_heap[0][0] <= start_time:
                _, prev_profit = heappop(min_heap)
                curr_profit = max(prev_profit, curr_profit)
            heappush(min_heap, (end_time, curr_profit + profit))
            max_profit = max(max_profit, curr_profit + profit)
        return max_profit


if __name__ == "__main__":
    job_scheduling = JobScheduling()
    print(job_scheduling.max_profit(
        [1, 2, 3, 4, 6],
        [3, 5, 10, 6, 9],
        [20, 20, 100, 70, 60]
    ))

