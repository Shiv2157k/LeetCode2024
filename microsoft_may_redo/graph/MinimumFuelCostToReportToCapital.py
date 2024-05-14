from typing import List
from collections import deque
from math import ceil


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree: List[int] = []


class ReportToCapital:

    def minimum_fuel_cost_required(self, roads: List[List[int]], seats: int) -> int:
        """
        Approach: BFS
        T: O(V + E)
        S: O(V + E)
        :param roads:
        :param seats:
        :return:
        """

        # Step 1: Build the graph with in degree and out degree
        graph = {}

        for road in roads:
            graph[road[0]] = graph.get(road[0], GraphNode())
            graph[road[0]].out_degree.append(road[1])
            graph[road[0]].in_degree += 1

            graph[road[1]] = graph.get(road[1], GraphNode())
            graph[road[1]].out_degree.append(road[0])
            graph[road[1]].in_degree += 1

        queue = deque()
        # add the in degree with one to queue to process
        for node in graph.keys():
            if graph[node].in_degree == 1 and node != 0:
                queue.append(node)

        # initialize a representative list with min fuel cost
        representatives = [1] * len(graph)
        # for tracking minimum fuel cost
        min_fuel_cost = 0

        while queue:

            node = queue.popleft()
            # calculate the fuel cost so far
            min_fuel_cost += ceil(representatives[node] / seats)

            # traverse through the neighbor representatives
            for neighbor in graph[node].out_degree:
                graph[neighbor].in_degree -= 1
                # calculate the representative fuel
                representatives[neighbor] += representatives[node]
                # if the in degree is 1 and neighbor is not 0 (capital city)
                if graph[neighbor].in_degree == 1 and neighbor != 0:
                    queue.append(neighbor)
        return min_fuel_cost
