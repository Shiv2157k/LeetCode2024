from typing import List


class Anagrams:

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: HashMap and hashset
        T: O(NK)
        S: O(NK)
        :param strs:
        :return:
        """

        anagrams = {}

        for word in strs:
            bucket = [0] * 26
            for char in word:
                bucket[ord(char) - ord('a')] += 1
            hash_val = hash(tuple(bucket))
            anagrams[hash_val] = anagrams.get(hash_val, [])
            anagrams[hash_val].append(word)

        result = []
        for key, values in anagrams.items():
            group = []
            for word in values:
                group.append(word)
            result.append(group)
        return result
