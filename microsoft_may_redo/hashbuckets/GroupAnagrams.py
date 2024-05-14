from typing import List


class Anagrams:

    def group(self, strs: str) -> List[List[int]]:
        """
        Approach: HashBucket
        T: O(N * M)
        S: O(N)
        :param strs:
        :return:
        """

        anagrams_map = {}

        for word in strs:
            bucket = [0] * 26
            for char in word:
                bucket[ord(char) - ord('a')] += 1
            hash_val = hash(tuple(bucket))
            anagrams_map[hash_val] = anagrams_map.get(hash_val, [])
            anagrams_map[hash_val].append(word)

        result = []

        for values in anagrams_map.values():
            anagrams = []
            for value in values:
                anagrams.append(value)
            result.append(anagrams)
        return result
