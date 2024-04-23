


class Strings:


    def multiply(self, num1: str, num2: str) -> str:
        """
        Approach: Text Book Math
        T: O(N)
        S: O(1)
        :param num1:
        :param num2:
        :return:
        """
        if '0' in {num1, num2}:
            return '0'

        result = [0] * (len(num1) + len(num2))

        for i1 in range(len(num1) - 1, -1, -1):
            for i2 in range(len(num2) - 1, -1, -1):

                digit = int(num1[i1]) * int(num2[i2])

                result[i1 + i2 + 1] += digit
                result[i1 + i2] += (result[i1 + i2 + 1] // 10)
                result[i1 + i2 + 1] = result[i1 + i2 + 1] % 10

        index = 0

        while index < len(result):
            if result[index] != 0:
                break
            index += 1
        return ''.join(map(str, result[index:]))

