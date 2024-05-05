from collections import deque
from typing import Deque, List, Dict
from math import ceil


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree: List[int] = []


class ReportToCapital:

    def minimum_fuel_cost(self, roads: List[List[int]], seats: int) -> int:
        """
        Approach: Deque
        T: O(N)
        S: O()
        :param roads:
        :param seats:
        :return:
        """

        graph: Dict[int, GraphNode] = {}

        for road in roads:
            graph[road[0]] = graph.get(road[0], GraphNode())
            graph[road[0]].out_degree.append(road[1])
            graph[road[0]].in_degree += 1

            graph[road[1]] = graph.get(road[1], GraphNode())
            graph[road[1]].out_degree.append(road[0])
            graph[road[1]].in_degree += 1

        queue: Deque[int] = deque()

        for node in range(1, len(roads) + 1):
            if graph[node].in_degree == 1:
                queue.append(node)

        # note: you need to count the total representatives involved
        # to know the fuel cost
        representatives: List[int] = [1] * (len(roads) + 1)
        fuel: int = 0

        while queue:
            node = queue.popleft()
            # fuel will increase if there are more reps and fewer seats
            fuel += ceil(representatives[node] / seats)

            for next_node in graph[node].out_degree:
                graph[next_node].in_degree -= 1
                # here we count the representatives
                representatives[next_node] += representatives[node]

                if graph[next_node].in_degree == 1 and next_node != 0:
                    queue.append(next_node)
        return fuel
