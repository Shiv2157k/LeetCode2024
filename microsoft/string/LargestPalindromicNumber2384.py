class PalindromicNumber:

    def longestPal(self, num: str) -> str:
        """
        Approach: Hash Map
        T: O(N)
        S: O(1)
        :param num:
        :return:
        """

        numFreq = {}
        firstHalf = []
        center = ''

        for digit in num:
            numFreq[digit] = numFreq.get(digit, 0) + 1

        for digit in range(9, -1, -1):

            digitChar = str(digit)

            if digitChar in numFreq:

                digitFreq = numFreq[digitChar]

                numPairs = digitFreq // 2

                if numPairs:
                    if not firstHalf and not digit:
                        numFreq['0'] = 1
                    else:
                        firstHalf.append(digitChar * numPairs)
                if digitFreq % 2 == 1 and not center:
                    center = digitChar

        if not center and not firstHalf:
            return "0"
        return "".join(firstHalf + [center] + firstHalf[::-1])


if __name__ == "__main__":
    palindromicNumber = PalindromicNumber()
    print(palindromicNumber.longestPal("444947137"))
    print(palindromicNumber.longestPal("00009"))
