from collections import deque
from typing import List


class GraphNode:

    def __init__(self):
        self.out_degree = set()
        self.in_degree = 0


class AlienDictionary:

    def print_alien_order(self, words: List[str]) -> str:
        """
        Approach: Kahn's Topological Sort with BFS
        T: O(C)
        S: O(1) or O(U+min(U^2,N))
        :param words:
        :return:
        """
        graph = {}

        # Step 0: Create structure with all unique nodes into graph
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = GraphNode()

        # Step 1: Build the edges and in degree nodes
        for index in range(1, len(words)):
            pre_word = words[index - 1]
            curr_word = words[index]
            # checking edge case if current word is prefix of previous word
            if len(curr_word) < len(pre_word) and curr_word.startswith(pre_word):
                return ""
            for pointer in range(min(len(pre_word), len(curr_word))):
                if pre_word[pointer] != curr_word[pointer]:
                    if curr_word[pointer] not in graph[pre_word[pointer]].out_degree:
                        graph[pre_word[pointer]].out_degree.add(curr_word[pointer])
                        graph[curr_word[pointer]].in_degree += 1
                    break

        # Step 2: Prepare the queue for BFS
        queue = deque()
        # add all the in degree zero chars to queue for traversal
        for key, graph_node in graph.items():
            if graph_node.in_degree == 0:
                queue.append(key)

        alien_order = []

        # Step 3: Perform BFS
        while queue:
            char = queue.popleft()
            alien_order.append(char)
            for next_char in graph[char].out_degree:
                graph[next_char].in_degree -= 1
                if graph[next_char].in_degree == 0:
                    queue.append(next_char)

        return "".join(alien_order) if len(alien_order) == len(graph) else ""


if __name__ == "__main__":
    alien_dictionary = AlienDictionary()
    print(alien_dictionary.print_alien_order(["wrt", "wrf", "er", "ett", "rftt", "te"]))
    print(alien_dictionary.print_alien_order(["z", "x", "z"]))
    print(alien_dictionary.print_alien_order(["ac", "ab", "zc", "zb"]))
