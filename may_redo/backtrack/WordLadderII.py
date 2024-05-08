from collections import defaultdict, deque
from typing import List, Set


class WordLadderII:

    def __init__(self):
        self.adj_list = defaultdict(list)
        self.curr_path = []
        self.shortest_path = []

    def find_ladders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        """
        Approach:
        T: O(NK^2 + alpha)
        S: O(NK)
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        word_set = set(word_list)
        self._breadth_first_search(begin_word, word_set)
        self.curr_path.append(end_word)
        self._backtrack(end_word, begin_word)
        return self.shortest_path

    def _backtrack(self, end_word: str, begin_word: str):

        if end_word == begin_word:
            self.shortest_path.append(self.curr_path[::-1])

        if end_word not in self.adj_list:
            return

        if end_word in self.adj_list:
            for word in self.adj_list[end_word]:
                self.curr_path.append(word)
                self._backtrack(word, begin_word)
                self.curr_path.pop()

    def _breadth_first_search(self, begin_word: str, word_set: Set[str]):

        queue = deque([begin_word])
        word_set.discard(begin_word)

        is_enqueued = {begin_word: 1}

        while queue:
            visited = []

            for _ in range(len(queue)):

                curr_word = queue.popleft()
                neighbors = self._build_neighbors(curr_word, word_set)

                for word in neighbors:
                    visited.append(word)

                    self.adj_list[word].append(curr_word)
                    if word not in is_enqueued:
                        queue.append(word)
                        is_enqueued[word] = 1
            for word in visited:
                word_set.discard(word)

    def _build_neighbors(self, word: str, word_set: Set[str]) -> List[str]:

        neighbors = []
        char_list = list(word)

        for i in range(len(word)):
            old_char = char_list[i]
            for c in range(ord('a'), ord('z') + 1):
                char_list[i] = chr(c)
                if char_list[i] != old_char and ''.join(char_list) in word_set:
                    neighbors.append(''.join(char_list))
            char_list[i] = old_char
        return neighbors
