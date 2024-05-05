from typing import List


class CatchABus:

    def get_latest_time(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        Approach: Sort and Single Pointer back and forth
        T: O(N log N)
        S: O(1)
        :param buses:
        :param passengers:
        :param capacity:
        :return:
        """

        # Step 1: Sort the bus for easy simulation
        buses.sort()
        passengers.sort()

        passenger_index: int = 0
        curr_capacity: int = 0

        # iterate through to see how many passengers bus can pick it up
        for arrival_time in buses:
            curr_capacity = capacity
            while (curr_capacity > 0 and passenger_index < len(passengers)
                   and passengers[passenger_index] <= arrival_time):
                curr_capacity -= 1
                passenger_index += 1

        # adjust the index back to the last passenger who boarded
        passenger_index -= 1

        # latest time to catch a bus depends on whether there is an empty seat in bus
        # case1: empty seat -> latest time is last bus time
        # case2: no empty seat -> last passenger boarded time
        latest_time = buses[-1] if curr_capacity > 0 else passengers[passenger_index]

        # find the unique time that is no other passenger arrived
        while passenger_index >= 0 and latest_time == passengers[passenger_index]:
            latest_time -= 1
            passenger_index -= 1
        return latest_time
