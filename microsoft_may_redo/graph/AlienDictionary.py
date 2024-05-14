from typing import List
from collections import deque


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree = []


class AlienDictionary:

    def alien_order(self, words: List[str]) -> str:
        """
        Approach: Khans Topological Sorting
        T: O(C)
        S: O(1) or O(U + min(U^2, N))
        :param words:
        :return:
        """

        graph = {}

        for word in words:
            for char in word:
                graph[char] = GraphNode()

        for index in range(1, len(words)):
            word = words[index - 1]
            next_word = words[index]

            if len(word) > len(next_word) and word.startswith(next_word):
                return ''

            for i in range(min(len(word), len(next_word))):
                if word[i] != next_word[i]:
                    if next_word[i] not in graph[word[i]].out_degree:
                        graph[word[i]].out_degree.append(next_word[i])
                        graph[next_word[i]].in_degree += 1
                    break

        queue = deque()
        for node, graph_node in graph.items():
            if graph_node.in_degree == 0:
                queue.append(node)
        results = []
        while queue:
            node = queue.popleft()
            results.append(node)
            for next_node in graph[node].out_degree:
                graph[next_node].in_degree -= 1
                if graph[next_node].in_degree == 0:
                    queue.append(next_node)
        return ''.join(results) if len(results) == len(graph) else ''
