class ZigZagConversion:

    def get_zig_zag(self, s: str, num_rows: int) -> str:
        """
        Approach: Simulation
        T: O(numRows * N)
        S: O(numRows * N)
        :param s:
        :param num_rows:
        :return:
        """

        result = [[] for _ in range(num_rows)]
        step = 1
        curr_row = 0

        for char in s:

            result[curr_row].append(char)
            curr_row += step

            if curr_row == num_rows or curr_row == 0:
                step *= -1

        output = ""
        for row in range(len(result)):
            output += "".join(result[row])
        return output
