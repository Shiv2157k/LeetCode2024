from typing import List
from collections import deque


class WordBreak:

    def is_word_break(self, s: str, word_list: List[str]):
        """
        Approach: BFS
        T: O(N^3 + m * k)
        Substring creation: O(N)
        Handling node costs: O(N^2)
        BFS cost: O(N^3)
        For set words creation: O(m . k)
        S: O(n + m + k)
        :param s:
        :param word_list:
        :return:
        """

        word_set = set(word_list)
        queue = deque([0])
        visited = {0}

        while queue:
            left = queue.popleft()

            if left == len(s):
                return True

            for right in range(left + 1, len(s) + 1):
                word = s[left: right]
                if word in word_set and right not in visited:
                    queue.append(right)
                    visited.add(right)
        return False