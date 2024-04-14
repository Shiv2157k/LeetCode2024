class Binary:

    def addV1(self, a: str, b: str) -> str:
        """
        Approach: Bit Manipulation
        T: O(max(N, M))
        S: O(max(N, M))
        :param a:
        :param b:
        :return:
        """

        x, y = int(a, 2), int(b, 2)

        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]

    def addV0(self, a: str, b: str) -> str:

        n = max(len(a), len(b))

        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):

            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                ans.append("1")
            else:
                ans.append("0")

            carry //= 2
        if carry == 1:
            ans.append("1")

        return "".join(ans[::-1])


if __name__ == "__main__":
    binary = Binary()
    print(binary.addV0("11", "1"))
    print(binary.addV0("1010", "1011"))
    print(binary.addV1("11", "1"))
    print(binary.addV1("1010", "1011"))
