from typing import List


class TaskScheduler:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Approach: HashBucket and Sort
        T: O(N)
        S: O(1)
        :param tasks:
        :param n:
        :return:
        """

        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()

        max_freq: int = freq[25] - 1
        idle_slots: int = max_freq * n

        for i in range(24, -1, -1):
            idle_slots -= min(max_freq, freq[i])
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
