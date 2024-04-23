from typing import List


class Anagrams:

    def group(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hash
        T: O(N)
        S: O(N)
        :param strs:
        :return:
        """

        anagrams = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            hashVal = hash(tuple(count))
            anagrams[hashVal] = anagrams.get(hashVal, [])
            anagrams[hashVal].append(word)
        output = []

        for key, values in anagrams.items():
            group = []
            for value in values:
                group.append(value)
            output.append(group)
        return output
