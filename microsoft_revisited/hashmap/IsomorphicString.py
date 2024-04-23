class IsomorphicString:

    def isIsomorphic(self, s: str, t: str) -> bool:

        hashOfs = self._transformString(s)
        hashOft = self._transformString(t)

        return hashOfs == hashOft

    def _transformString(self, string: str) -> str:

        indexMap = {}
        newStr = []

        for index, char in enumerate(string):
            if char not in indexMap:
                indexMap[char] = index
            newStr.append(str(indexMap[char]))
        return ''.join(newStr)
