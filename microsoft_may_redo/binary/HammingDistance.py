

class HammingDistance:

    def hamming_distance(self, x: int, y: int) -> int:
        """
        Approach:
        :param x:
        :param y:
        :return:
        """

        diff = x ^ y
        dist = 0

        while diff > 0:
            diff &= diff - 1
            dist += 1
        return dist