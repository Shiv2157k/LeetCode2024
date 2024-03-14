

class BinarySubSeq:

    def unique(self, binary: str) -> int:
        """
        Approach: Dynamic Programming
        T: O(N)
        S: O(N)
        :param binary:
        :return:
        """

        size = len(binary)
        one_index = 0

        # to find out the leading one index as we do not care about leading zeroes
        while one_index < size and binary[one_index] == '0':
            one_index += 1

        if one_index == size:
            return 1

        # build the dp
        dp = [0] * size
        # mark the first index with one to one
        dp[one_index] = 1

        # to capture previous zero and one index to eliminate duplicate subsequences
        last_zero = last_one = 0

        for index in range(one_index + 1, size):

            dup_index = last_zero if binary[index] == '0' else last_one
            dup_sum = dp[dup_index - 1] if dup_index > 0 else 0

            # dp state transition
            # Every time a new element comes in the subsequence increase twice
            # eliminating the duplicate elements and its subsequence
            # as we want to capture count of unique good subsequence
            dp[index] = (dp[index - 1] * 2) - dup_sum

            # capture the previous seen zero and one index
            if binary[index] == '0':
                last_zero = index
            else:
                last_one = index

        # to remember -> need to consider single zero as a unique good sequence
        has_zero = 0
        mod = 10**9 + 7
        if '0' in binary:
            has_zero = 1

        return (dp[-1] + has_zero) % mod


if __name__ == "__main__":
    binary_sub_seq = BinarySubSeq()
    print(binary_sub_seq.unique("101"))
    print(binary_sub_seq.unique("10101"))
    print(binary_sub_seq.unique("111"))
    print(binary_sub_seq.unique("11"))
    print(binary_sub_seq.unique("10"))
    print(binary_sub_seq.unique("1"))
    print(binary_sub_seq.unique("0"))