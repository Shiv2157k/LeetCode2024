from collections import deque
from typing import List, Dict


class WordLadder:

    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Approach: BFS
        T: O(M^2 * N)
        S: O(M^2 * N)
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """

        if end_word not in word_list or not end_word or not begin_word or not word_list:
            return 0

        all_combo_dict = self._generate_possible_combination_dict(word_list)

        queue = deque([(begin_word, 1)])
        visited = {begin_word: True}

        while queue:
            curr_word, level = queue.popleft()

            for i in range(len(begin_word)):

                intermediate_word = curr_word[:i] + '*' + curr_word[i + 1:]
                if intermediate_word in all_combo_dict:
                    for neighbor in all_combo_dict[intermediate_word]:
                        if neighbor == end_word:
                            return level + 1
                        if neighbor not in visited:
                            queue.append((neighbor, level + 1))
                            visited[neighbor] = True
                    all_combo_dict[intermediate_word] = []
        return 0

    def _generate_possible_combination_dict(self, word_list: List[str]) -> Dict[str, List[str]]:
        combo_dict = {}

        for word in set(word_list):

            for i in range(len(word)):
                possible_word = word[:i] + '*' + word[i + 1:]
                combo_dict[possible_word] = combo_dict.get(possible_word, [])
                combo_dict[possible_word].append(word)
        return combo_dict
