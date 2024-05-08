class AngleBetweenHandsOfAClock:

    def angle_clock(self, hour: int, minutes: int):
        """
        Approach: Math
        T: O(1)
        S: O(1)
        :param hour:
        :param minutes:
        :return:
        """
        # total clock is 360 degrees
        # total 60 minutes in clock
        # 1 min = 6 degrees 360 / 60
        # total 12 hours in clock
        # 1 hour = 30 degrees 360 / 12 = 30

        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = one_min_angle * minutes
        # do mod for hour to handle 1 hour edge case
        hours_angle = (hour % 12 + minutes / 60) * one_hour_angle

        diff = abs(hours_angle - minutes_angle)
        return min(diff, 360 - diff)
