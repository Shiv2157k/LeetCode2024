class ZigZag:

    def convertV1(self, s: str, numRows: int) -> str:
        """
        Aprpoach: Jump
        T: O(N)
        S: O(1)
        :param s:
        :param numRows:
        :return:
        """

        if numRows == 1 or len(s) <= numRows:
            return s
        n = len(s)
        charsInSection = 2 * (numRows - 1)
        output = []

        for currRow in range(numRows):
            index = currRow
            while index < n:
                output.append(s[index])
                if currRow != 0 and currRow != numRows - 1:
                    charsInBetween = charsInSection - 2 * currRow
                    secondIndex = charsInBetween + index
                    if secondIndex < n:
                        output.append(s[secondIndex])
                index += charsInSection
        return "".join(output)

    def convertV0(self, s: str, numRows: int) -> str:
        """
        Approach:
        T: O(numRows * n)
        S: O(numRows * n)
        :param s:
        :return:
        """

        # base case
        if numRows == 1 or len(s) <= numRows:
            return s

        result = [[] for _ in range(numRows)]
        currRow = 0
        step = 1

        for char in s:

            result[currRow].append(char)
            currRow += step
            if currRow == 0 or currRow == numRows - 1:
                step = -step

        output = ''
        for row in result:
            output += ''.join(row)
        return output


if __name__ == "__main__":
    zigzag = ZigZag()
    print(zigzag.convertV0("PAYPALISHIRING", 3))
    print(zigzag.convertV1("PAYPALISHIRING", 3))
