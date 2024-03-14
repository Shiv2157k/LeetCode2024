import heapq
from collections import defaultdict, deque
from typing import List


class Flights:
    """
    n = 4, flights = [
            src   dst   price/ distance
            [0,     1,  100],
            [1,     2,  100],
            [2,     0,  100],
            [1,     3,  600],
            [2,     3,  200]
        ], src = 0, dst = 3, k = 1
    Output: 700
    """

    def cheapest_within_k_stops(self, n: int, flights: List[List[int]], src: int, dest: int, k: int) -> int:
        """
        Approach: BFS
        T: O(N + E*K)
        S: O(N + E*K)
        :param n:
        :param flight:
        :param src:
        :param dest:
        :param k:
        :return:
        """
        # Step 1: build the neighbor with all the nodes
        neighbors = defaultdict(list)
        for source, destination, price in flights:
            neighbors[source].append((destination, price))
        # Step 2: create a list with prices/ distances whatever we want to call this helps with the comparison
        #         - initialize the list with highest value as we want to store the min values
        prices = [float("inf")] * n
        # Step 3: store the source and price/ distance in the queue
        queue = deque()
        # initialize the queue with the start node and price to 0
        queue.append((src, 0))

        # Step 3: Iterate over the heap with constraint k
        while queue and k >= 0:
            # capture the length of queue for iteration
            qlen = len(queue)
            # iterate over the queue and its neighbors
            for _ in range(qlen):
                # pop the src and price
                curr_node, curr_price = queue.popleft()
                for node, price in neighbors[curr_node]:
                    # Step 4: check the min price and update it to the prices list
                    if curr_price + price < prices[node]:
                        prices[node] = curr_price + price
                        queue.append((node, curr_price + price))
            # decrease k as we reach each level in bfs
            k -= 1
        return prices[dest] if prices[dest] != float("inf") else -1

    def cheapest_within_k_stops_v1(self, n: int, flights: List[List[int]], src: int, dest: int, k: int) -> int:
        """
        Approach: Bell Ford
        Concept of bell ford is that if there are n nodes,
        max steps required to reach destination is n - 1
        T: O((N + E)*K)
        S: O(N)
        :param n:
        :param flight:
        :param src:
        :param dest:
        :param k:
        :return:
        """
        # Things to note:
        # - we don't need neighbors here
        #  we iterate based on k steps
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            # make a copy to keep track of previous prices
            temp = prices.copy()
            for src, des, price in flights:
                if prices[src] != float("inf"):
                    temp[des] = min(prices[src] + price, temp[des])
            prices = temp.copy()
        return prices[dest] if prices[dest] != float("inf") else -1

    def cheapest_within_k_stops_v2(self, n: int, flights: List[List[int]], src: int, dest: int, k: int) -> int:
        """
        Approach: BFS
        T:
        O:
        :param n:
        :param flight:
        :param src:
        :param dest:
        :param k:
        :return:
        """
        # Step 1: build the neighbor and visited set to track if we have already visited
        visited = {}
        neighbors = {source: [] for source in range(n)}
        for source, destination, price in flights:
            neighbors[source].append((destination, price))

        # We use heap to pick up the next nodes
        min_heap = []
        # price, node, stops
        heapq.heappush(min_heap, (0, src, 0))

        while min_heap:

            curr_price, source, curr_stops = heapq.heappop(min_heap)
            visited[source] = curr_stops
            if source == dest:
                return curr_price
            if curr_stops > k:
                continue

            for neighbor, price in neighbors[source]:
                if neighbor in visited and visited[neighbor] <= curr_stops:
                    continue
                heapq.heappush(min_heap, (curr_price + price, neighbor, curr_stops + 1))
        return -1


if __name__ == "__main__":
    air = Flights()
    print(air.cheapest_within_k_stops_v2(

        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    ))
    print(air.cheapest_within_k_stops_v1(

        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    ))
    print(air.cheapest_within_k_stops(

        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    ))
    print(air.cheapest_within_k_stops_v2(

        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
    ))
