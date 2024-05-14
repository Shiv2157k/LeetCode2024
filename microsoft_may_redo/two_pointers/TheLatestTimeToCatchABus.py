from typing import List


class CatchABus:

    def latest_time_to_catch(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        Approach: Two Pointers
        T: O(N log N + M log M)
        S: O(1) -> for sorting takes O(N) in python as it uses Timsort
        :param buses:
        :param passengers:
        :param capacity:
        :return:
        """

        buses.sort()
        passengers.sort()

        passengers_ptr = 0
        curr_capacity = 0

        for arrival_time in buses:
            curr_capacity = capacity

            while curr_capacity > 0 and passengers_ptr < len(passengers) and passengers[passengers_ptr] <= arrival_time:
                curr_capacity -= 1
                passengers_ptr += 1

        # move back to time last passenger above took the bus
        passengers[passengers_ptr] -= 1

        latest_time = buses[-1] if curr_capacity > 0 else passengers_ptr[passengers_ptr]

        while passengers_ptr >= 0 and passengers[passengers_ptr] == latest_time:
            latest_time -= 1
            passengers_ptr -= 1
        return latest_time
