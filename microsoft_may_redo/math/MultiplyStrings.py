class MultiplyStrings:

    def multiply(self, num1: str, num2: str) -> str:
        """
        Approach: Mulitply Schoolbook
        T: O(MN)
        S: O(N)
        :param num1:
        :param num2:
        :return:
        """
        if '0' in {num1, num2}:
            return '0'

        result = [0] * (len(num1) + len(num2))

        for p1 in range(len(num1) - 1, -1, -1):
            for p2 in range(len(num2) - 1, -1, -1):
                v1 = ord(num1[p1]) - ord('0')
                v2 = ord(num2[p2]) - ord('0')

                digit = v1 * v2

                result[p1 + p2 + 1] += digit
                result[p1 + p2] += (result[p1 + p2 + 1] // 10)
                result[p1 + p2 + 1] %= 10

        pointer = 0
        output = []

        while pointer < len(result):
            if result[pointer] != 0:
                break
            pointer += 1
        while pointer < len(result):
            output.append(str(result[pointer]))
            pointer += 1
        return ''.join(output)
