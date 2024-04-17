from heapq import heappop, heappush
from typing import List


class TaskScheduler:

    def leastIntervalV2(self, tasks: List[str], n: int) -> int:
        """
        Approach: Pure Greedy
        T: O(N)
        S: O(N)
        :param tasks:
        :param n:
        :return:
        """

        freq = [0] * 26
        maxFreq = 0
        maxFreqOccurrence = 0

        for task in tasks:
            hashKey = ord(task) - ord('A')
            freq[hashKey] += 1

            if maxFreq == freq[hashKey]:
                maxFreqOccurrence += 1
            elif maxFreq < freq[hashKey]:
                maxFreq = freq[hashKey]
                maxFreqOccurrence = 1

        # calculation part
        partCount = maxFreq - 1
        partLength = n - (maxFreqOccurrence - 1)
        emptySlots = partCount * partLength
        availableTasks = len(tasks) - (maxFreqOccurrence * maxFreq)
        idles = max(0, emptySlots - availableTasks)
        
        return len(tasks) + idles

    def leastIntervalV1(self, tasks: List[str], n: int) -> int:
        """
        Approach: Sort Frequency
        T: O(26 log 26 + N)
        S: O(26) -> O(1)
        :param tasks:
        :param n:
        :return:
        """

        freq = [0] * 26

        # calculate the freq
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # sort the freq in non-decreasing order
        freq.sort()
        # maxFreq is one less than high freq
        maxFreq = freq[25] - 1

        # idleSlots ideal is maxFreq * n
        idleSlots = maxFreq * n

        # iterate through and decrement the idle slots
        for i in range(24, -1, -1):
            idleSlots -= min(maxFreq, freq[i])
        return len(tasks) + idleSlots if idleSlots > 0 else len(tasks)

    def leastIntervalV0(self, tasks: List[str], n: int) -> int:
        """
        Approach: MaxHeap
        T: O(N)
        S: O(N)
        :param tasks:
        :param n:
        :return:
        """

        freq = [0] * 26

        # calculate the freq
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # push the freq to the heap
        # for maxHeap negate the freq
        maxHeap = []
        for i in range(26):
            if freq[i] > 0:
                heappush(maxHeap, -freq[i])

        # iterate through the heap until it is empty
        # calculate overall time it took
        time = 0
        while maxHeap:
            # we need to go through the cycle when
            # we still have tasks in heap
            # each cycle is n + 1
            cycle = n + 1
            taskCount = 0
            nextRound = []

            # cycle through as long as below meets
            while maxHeap and cycle > 0:
                newFreq = -heappop(maxHeap)
                if newFreq > 1:
                    nextRound.append(-(newFreq - 1))
                cycle -= 1
                taskCount += 1

            # prepare for next cycle
            for updatedFreq in nextRound:
                heappush(maxHeap, updatedFreq)
            time += taskCount if not maxHeap else n + 1
        return time

