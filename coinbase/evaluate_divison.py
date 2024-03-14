from collections import defaultdict, deque
from typing import List, Set


class Evaluate:

    def by_divison_of_queries_v0(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Approach: DFS
        T: O(M * N)
        S: O(N)
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        graph = defaultdict(defaultdict)

        def back_track(curr_node: str, target_node: str, acc_weight: float, visited: Set) -> float:
            visited.add(curr_node)
            output = -1.0
            if target_node in graph[curr_node]:
                return acc_weight * graph[curr_node][target_node]

            for neighbor, weight in graph[curr_node].items():
                if neighbor not in visited:
                    output = back_track(neighbor, target_node, acc_weight * weight, visited)
                    if output != -1.0:
                        break
            visited.remove(curr_node)
            return output

        # Step 1: Build Graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        result = []

        # Step 2: Evaluate each query
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                result.append(-1.0)
            elif dividend == divisor:
                result.append(1.0)
            else:
                visited = set()
                output = back_track(dividend, divisor, 1.0, visited)
                result.append(output)
        return result

    def by_divison_of_queries_v1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        # Step 1: Build the graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        results = []

        # Step 2: Evaluate the queries
        for dividend, divisor in queries:
            # base cases
            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
                continue
            if dividend == divisor:
                results.append(1.0)
                continue

            queue = deque()
            # source, it value is by default 1.0
            queue.append([dividend, 1.0])
            visited = set()
            visited.add(dividend)
            # perform BFS
            while queue:
                curr_node, accumulated_weight = queue.popleft()
                if divisor in graph[curr_node]:
                    results.append(accumulated_weight * graph[curr_node][divisor])
                    break  # reached destination

                # traverse through next neighbors from source
                for neighbor, weight in graph[curr_node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, accumulated_weight * weight))
                        visited.add(curr_node)
            else:  # there is no valid path
                results.append(-1.0)
        return results









if __name__ == "__main__":
    evaluate = Evaluate()
    print(evaluate.by_divison_of_queries_v0(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ))