class WildCard:

    def isMatchV1(self, s: str, p: str) -> bool:
        """
        Approach: BackTrack
        T: O(min(S, P) -> WorstCase : O(S * P)
        S: O(1)
        :param s:
        :param p:
        :return:
        """

        pLen, sLen = len(p), len(s)
        pPtr, sPtr = 0, 0
        starPtr, sTempPtr = -1, -1

        while sPtr < sLen:
            # If the pattern character = string character
            # or pattern character = '?'
            if pPtr < pLen and p[pPtr] in {"?", s[sPtr]}:
                pPtr += 1
                sPtr += 1
            # If pattern character = '*'
            elif pPtr < pLen and p[pPtr] == "*":
                starPtr = pPtr
                sTempPtr = sPtr
                pPtr += 1
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif starPtr == -1:
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                pPtr = starPtr + 1
                sPtr = sTempPtr + 1
                sTempPtr = sPtr

        while pPtr < pLen:
            if p[pPtr] != "*":
                return False
            pPtr += 1
        return True

    def isMatchV0(self, s: str, p: str) -> bool:
        """
        Approach: Recursion with memo
        T: O()
        S: O()
        :param s:
        :param p:
        :return:
        """

        def refinePattern(p: str) -> str:
            filterPattern = []
            for char in p:
                if not filterPattern or char != "*":
                    filterPattern.append(char)
                elif filterPattern[-1] != "*":
                    filterPattern.append(char)
            return "".join(filterPattern)

        def memoSolve(s: str, p: str) -> bool:

            if (s, p) in memo:
                return memo[(s, p)]

            if p == s or p == "*":
                memo[(s, p)] = True
            elif p == "" or s == "":
                memo[(s, p)] = False
            elif p[0] == s[0] or p[0] == "?":
                memo[(s, p)] = memoSolve(s[1:], p[1:])
            elif p[0] == "*":
                memo[(s, p)] = memoSolve(s[1:], p) or memoSolve(s, p[1:])
            else:
                memo[(s, p)] = False
            return memo[(s, p)]

        memo = {}
        p = refinePattern(p)
        return memoSolve(s, p)


if __name__ == "__main__":
    wildCard = WildCard()
    print(wildCard.isMatchV0("mississippi", "m??*ss*?i*pi"))
    print(wildCard.isMatchV0("adcbdk", "*a*b?k"))

    print(wildCard.isMatchV1("mississippi", "m??*ss*?i*pi"))
    print(wildCard.isMatchV1("adcbdk", "*a*b?k"))
