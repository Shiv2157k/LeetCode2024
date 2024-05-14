from typing import List, Set
from collections import deque


class EvaluateDivision:

    def calculate_equation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:
        """
        Approach: Graph and (DFS or backtrack)
        T: O(M * N)
        S: O(N)
        :param equations:
        :param values:
        :param queries:
        :return:
        """

        def backtrack(curr_node: str, target_node: str, cumm_product: int, visited: Set):

            visited.add(curr_node)
            curr_output = -1.0
            if curr_node in graph:
                if target_node in graph[curr_node]:
                    curr_output = cumm_product * graph[curr_node][target_node]
                else:
                    if target_node in graph[curr_node]:
                        for next_node, val in graph[curr_node].items():
                            if next_node in visited:
                                continue
                            curr_output = backtrack(next_node, target_node, val * cumm_product, visited)
                            if curr_output != -1.0:
                                break
            visited.remove(curr_node)
            return curr_output

        graph = {}
        for i in range(len(values)):

            dividend = equations[i][0]
            divisor = equations[i][1]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        results = []

        for dividend, divisor in queries:

            if dividend not in graph or divisor not in graph:
                output = -1.0
            elif dividend == divisor:
                output = 1.0
            else:
                visited = set()
                output = backtrack(dividend, divisor, 1, visited)
            results.append(output)
        return results

    def calculate_equation_v0(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:

        graph = {}

        for i in range(len(values)):
            dividend = equations[i][0]
            divisor = equations[i][1]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        results = []

        for dividend, divisor in queries:

            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
                continue
            if dividend == divisor:
                results.append(1.0)
                continue

            queue = deque([(dividend, 1.0)])
            visited = {dividend}

            while queue:

                curr_node, acc_weight = queue.popleft()
                if divisor in graph[curr_node]:
                    results.append(acc_weight * graph[curr_node][divisor])
                    break

                for next_node, weight in graph[curr_node].items():
                    if next_node not in visited:
                        queue.append((next_node, acc_weight * weight))
                        visited.add(curr_node)
            else:
                results.append(-1.0)
        return results
