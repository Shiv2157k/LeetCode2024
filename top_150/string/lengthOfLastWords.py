

class LastWord:


    def getLengthV0(self, s: str) -> int:
        """
        Approach: Two Pass
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        p = len(s) - 1

        while p >= 0 and s[p] == " ":
            p -= 1

        length = 0

        while p >= 0 and s[p] != " ":
            length += 1
            p -= 1
        return length

    def getLengthV1(self, s: str) -> int:
        """
        Approach: Single Pass
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        pointer = len(s)
        length = 0

        while pointer > 0:
            pointer -= 1

            if s[pointer] != " ":
                length += 1
            elif length > 0:
                return length
        return length


if __name__ == "__main__":
    lastWord = LastWord()
    print(lastWord.getLengthV0("  Hello   World   "))
    print(lastWord.getLengthV1("  Hello   World   "))