from typing import List
from collections import deque


class WordBreak:

    def word_break(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: BFS
        T: O(n^3 + m * k)
        S: O(n + m * k)
        :param s:
        :param wordDict:
        :return:
        """

        word_set = set(wordDict)
        queue = deque([0])
        visited = set()
        visited.add(0)

        while queue:
            left = queue.popleft()
            if left == len(s):
                return True
            for right in range(left + 1, len(s) + 1):
                if s[left: right] in word_set:
                    if right not in visited:
                        queue.append(right)
                        visited.add(right)
        return False
