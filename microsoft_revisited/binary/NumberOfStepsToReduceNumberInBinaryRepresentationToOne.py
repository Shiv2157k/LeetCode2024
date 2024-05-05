class BinaryRepresentation:

    def steps_to_reduce_to_one(self, s: str) -> int:
        """
        Approach: Right most Bit
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):

            right_most_bit = ord(s[i]) - ord('0')
            # even then it will be two steps
            if right_most_bit + carry == 1:
                carry = 1
                steps += 2
            else:  # odd it will be one step
                steps += 1
        return steps + carry
