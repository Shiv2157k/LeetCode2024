from collections import defaultdict
from typing import List
from pprint import pprint


class Anagrams:

    def group_together_v1(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: HashTable and Sort
        T: O(NK log K)
        S: O(NK)
        :param strs:
        :return:
        """
        # ans = defaultdict(list)
        anagrams = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            hash_val = hash(tuple(count))
            if hash_val not in anagrams:
                anagrams[hash_val] = [word]
            else:
                anagrams[hash_val].append(word)
        return anagrams.values()


    def group_together_v0(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: HashTable and Sort
        T: O(NK log K)
        S: O(NK)
        :param strs:
        :return:
        """
        ans = defaultdict(list)
        for word in strs:
            ans["".join(sorted(word))].append(word)
        return ans.values()


if __name__ == "__main__":
    anagrams = Anagrams()
    pprint(anagrams.group_together_v0(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ))
    pprint(anagrams.group_together_v1(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ))
    pprint(anagrams.group_together_v0(
        [""]
    ))
    pprint(anagrams.group_together_v1(
        [""]
    ))
    pprint(anagrams.group_together_v0(
        ["a"]
    ))
    pprint(anagrams.group_together_v1(
        ["a"]
    ))