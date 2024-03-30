class Anagrams:

    def isValid(self, s: str, t: str) -> bool:
        """
        Approach: Hash Map
        T: O(N)
        S: O(1) -> this is fixed length
        :param s:
        :param t:
        :return:
        """

        freqMap = [0] * 26
        for char in s:
            # hashChar = hash(char)
            # freqMap[hashChar] += 1
            charInt = ord(char) - ord('a')
            freqMap[charInt] += 1

        for char in t:
            charInt = ord(char) - ord('a')
            freqMap[charInt] -= 1
            if freqMap[charInt] < 0:
                return False
        return True


if __name__ == "__main__":
    anagram = Anagrams()
    print(anagram.isValid("anagram", "naagram"))
    print(anagram.isValid("anagram", "naagrap"))
    print(anagram.isValid("any", "nya"))
