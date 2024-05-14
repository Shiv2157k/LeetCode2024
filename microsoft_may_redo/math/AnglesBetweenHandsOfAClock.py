


class Clock:

    def angle_clock(self, hour: int, minutes: int) -> float:
        """
        Approach: Math
        T: O(1)
        S: O(1)
        :param hour:
        :param minutes:
        :return:
        """

        # 60 needles in a minute -> 360degrees total clock
        # 360 / 60 -> 6  degrees for 1st minute
        # 12 hour needles in a hour
        # 360 / 12 = 30 degrees for an hour

        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = minutes * 6
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

        diff = abs(hour_angle - minutes_angle)
        
        return min(diff, 360 - diff)