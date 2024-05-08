class PermutationSequence:

    def get_permutation(self, n: int, k: int) -> str:
        """
        Approach: Math Factorial
        T: O(N ^ 2) -> For deletion
        N + (N - 1) + ... + 1 = N(N - 1) / 2
        S: O(N)
        :param n:
        :param k:
        :return:
        """

        # factorials
        factorials = [1]
        # permutation -> initial state build
        init_sequence = ['1']

        # generate the factorial from 0 -> n - 1
        # generate the initial state of permutation sequence 1 -> n
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            init_sequence.append(str(i + 1))

        # to fit k in 0...n! - 1
        k -= 1
        curr_seq = []

        # traverse from back for the MSD - Most Significant Digit
        for i in range(n - 1, -1, - 1):
            block_and_index = k // factorials[i]
            k -= block_and_index * factorials[i]

            # add the output
            curr_seq.append(init_sequence[block_and_index])

            # narrow down the sequence as we move right from right most digit
            del init_sequence[block_and_index]
        return ''.join(curr_seq)
