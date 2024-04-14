class PermutationSequence:

    def getPermutation(self, n: int, k: int) -> str:
        """
        Approach: Factorial and MAth
        T: O(N^2) as for deletion N + (N - 1) .. = N(N - 1)/2
        S: O(N)
        :param n:
        :param k:
        :return:
        """

        factorials, nums = [1], ['1']

        # build factorial
        for num in range(1, n):
            # 1!, 2!...(n - 1)!
            factorials.append(factorials[num - 1] * num)
            # 1, 2, 3....n
            nums.append(str(num + 1))

        # to fit into 0...n - 1
        k -= 1
        ans = []
        for num in range(n - 1, -1, -1):
            # to find the index
            idx = k // factorials[num]
            # move on to the next most significant bit
            k -= idx * factorials[num]

            ans.append(nums[idx])
            del nums[idx]
        return ''.join(ans)


if __name__ == "__main__":
    permSeq = PermutationSequence()
    print(permSeq.getPermutation(3, 3))