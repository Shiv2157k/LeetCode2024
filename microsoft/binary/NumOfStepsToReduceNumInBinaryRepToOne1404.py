class BinaryRepresentation:

    def numSteps(self, s: str) -> int:

        countSteps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):

            rightMostBit = ord(s[i]) - ord('0')
            # if it is an odd need to perform two operations
            # 2- make it even
            # 2 - divide by 2
            if rightMostBit + carry == 1:
                carry = 1
                countSteps += 2
            # even just one operation
            else:
                countSteps += 1
        # since left most is one
        return countSteps + carry
