class AddBinary:

    def add_binary_v1(self, a: str, b: str) -> str:
        """
        Approach: Bit Manipulation
        T: O(N)
        S: O(1)
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

    def add_binary_v0(self, a: str, b: str) -> str:
        """
        Approach: MAth
        T: O(N)
        S: O(N)
        :param a:
        :param b:
        :return:
        """

        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):

            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
            carry //= 2

        if carry == 1:
            ans.append('1')

        return ''.join(ans[::-1])
