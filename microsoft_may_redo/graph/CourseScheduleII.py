from typing import List, Dict
from collections import deque


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree = []


class CourseScheduleII:

    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Approach: Khan's Topological Sort
        T: O(N + M)
        S: O(N + M)
        :param num_courses:
        :param prerequisites:
        :return:
        """

        graph: Dict[int, GraphNode] = {}

        for course, pre_req in prerequisites:
            graph[course] = graph.get(course, GraphNode())
            graph[course].in_degree += 1

            graph[pre_req] = graph.get(pre_req, GraphNode())
            graph[pre_req].out_degree.append(course)

        queue = deque()
        course_order = []

        for course in range(num_courses):
            if course in graph and graph[course].in_degree == 0:
                queue.append(course)
            elif course not in graph:
                course_order.append(course)

        while queue:

            curr_course = queue.popleft()
            course_order.append(curr_course)

            for next_course in graph[curr_course].out_degree:
                graph[next_course].in_degree -= 1
                if graph[next_course].in_degree == 0:
                    queue.append(next_course)
        return course_order if len(course_order) == num_courses else []
