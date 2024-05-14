class BinaryNumberToOne:

    def number_of_steps(self, s: str) -> int:
        """
        Approach: RightMost bit with carry
        Rules:
        - If the current number is even, you have to divide it by 2.
        - If the current number is odd, you have to add 1 to it.
        Logic:
        - Binary Representation of any even number ends with 0
        - Binary Representation of any even number ends with 1

        - if we have odd decimal, say 13 we need to add 1
        - if we have even decimal, say 12 we need to divide it by 2
        From above,
        1. whenever we have a odd no. we have to do two operations
        - add 1 -> carry becomes 1
        - divide by 2
        2. whenever we have even no. we have to do 1 operation
        - divide by 2

        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        count_steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):

            right_most_bit = ord(s[i]) - ord('0')

            # even
            if right_most_bit + carry == 1:
                carry = 1
                count_steps += 2
            else:
                count_steps += 1
        return count_steps + carry
