class Multiply:

    def twoStrings(self, nums1: str, nums2: str):
        """
        Approach: Sum the Products from all pairs of digits
        T: O(M * N)
        S: O(M + N)
        :param nums1:
        :param nums2:
        :return:
        """

        if "0" in {nums1, nums2}:
            return "0"

        l1, l2 = len(nums1), len(nums2)
        result = [0] * (l1 + l2)

        for i1 in range(l1 - 1, -1, -1):
            for i2 in range(l2 - 1, -1, -1):
                digit = int(nums1[i1]) * int(nums2[i2])
                # adding the whole digit
                result[i1 + i2 + 1] += digit
                # adding carry to the next index from back
                result[i1 + i2] += result[i1 + i2 + 1] // 10
                # trimming out the left side number if this is two-digit number
                result[i1 + i2 + 1] = result[i1 + i2 + 1] % 10

        index = 0

        while index < (l1 + l2):
            if result[index] != 0:
                break
            index += 1

        return "".join(map(str, result[index:]))


if __name__ == "__main__":
    multiply = Multiply()
    print(multiply.twoStrings("123", "456"))
    print(multiply.twoStrings("25", "25"))
    print(multiply.twoStrings("3", "2"))
    print(multiply.twoStrings("10", "10"))
    print(multiply.twoStrings("7", "7"))
