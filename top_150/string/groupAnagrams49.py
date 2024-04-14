from typing import List


class Anagrams:

    def group(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hash Table and hash values
        T: O(NK)
        S: O(NK
        :param strs:
        :return:
        """

        anagramMap = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            anagramMap[key] = anagramMap.get(key, [])
            anagramMap[key].append(word)
        return anagramMap.values()


if __name__ == "__main__":
    anagrams = Anagrams()
    print(anagrams.group(["eat", "tea", "tan", "ate", "nat", "bat"]))
