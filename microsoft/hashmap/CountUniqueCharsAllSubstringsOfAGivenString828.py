class CountUniqueChars:

    def uniqueLetterString(self, s: str) -> int:

        mod = 10 ** 7

        n = len(s)

        # build the map with
        hashMap = [[] for _ in range(26)]

        # store the leftmost index i.e., -1
        for i in range(26):
            hashMap[i].append(-1)

        # store all the indices of s
        for i in range(n):
            hashMap[ord(s[i]) - ord('A')].append(i)

        # store the right most index i.e., total length
        for i in range(26):
            hashMap[i].append(n)

        # calculate the count i.e., cross product of ....c.... => leftbound * rightbound
        count = 0
        for i in range(26):
            for j in range(1, len(hashMap[i]) - 1):
                #  => leftbound * rightbound
                count += (hashMap[i][j] - hashMap[i][j - 1]) * (hashMap[i][j + 1] - hashMap[i][j])
        return count % mod


if __name__ == "__main__":
    cUc = CountUniqueChars()
    print(cUc.uniqueLetterString("ABCABDA"))
