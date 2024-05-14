from typing import List, Dict
from collections import deque


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree = []


class CourseSchedule:

    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: Khan's Topological Sorting
        T: O(M + N)
        S: O(M + N)
        :param num_courses:
        :param prerequisites:
        :return:
        """
        # 1 -> 0
        graph: Dict[int, GraphNode] = {}

        for course, pre_req in prerequisites:
            graph[course] = graph.get(course, GraphNode())
            graph[course].in_degree += 1

            graph[pre_req] = graph.get(pre_req, GraphNode())
            graph[pre_req].out_degree.append(course)

        queue = deque()
        courses_taken = 0

        for course in range(num_courses):
            if course in graph and graph[course].in_degree == 0:
                queue.append(course)
            elif course not in graph:
                courses_taken += 1

        while queue:
            curr_course = queue.popleft()
            courses_taken += 1

            for next_course in graph[curr_course].out_degree:
                graph[next_course].in_degree -= 1
                if graph[next_course].in_degree == 0:
                    queue.append(next_course)
        return courses_taken == num_courses
