from collections import deque
from typing import List


class ZigZagIteratorV0:
    """
    Approach: Two Pointers -> Vertical and Horizontal
    T: O(N)
    S: O(N)
    """

    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        # vertical pointer for traversing vectors
        self.vector_pointer = 0
        # horizontal pointer for traversing elements in vector
        self.element_pointer = 0
        # to track current counter
        self.current_counter = 0
        # total elements combining all the vector elements
        self.total_elements = len(v1) + len(v2)

    def next(self) -> int:
        iter_next = 0
        result = None
        while iter_next < self.total_elements:
            # fetch the current vector
            curr_vector = self.vectors[self.vector_pointer]
            # check whether current vector length is valid
            if iter_next < len(curr_vector):
                result = curr_vector[self.element_pointer]
            self.vector_pointer = (self.vector_pointer + 1) % len(self.vectors)
            # if the vector pointer is 0 increment the element pointer
            if self.vector_pointer == 0:
                self.element_pointer += 1
            # increment the current counter
            if result is not None:
                self.current_counter += 1
            # return the element
            return result
        raise Exception("No more elements")

    def hasNext(self) -> bool:
        return self.current_counter < self.total_elements


class ZigZagIteratorV1:
    """
    Approach: Using Queues which acts as both the pointers
    T: O(1)
    S: O(K)
    """

    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()
        self.total_elements = len(v1) + len(v2)

        for index, vector in enumerate(self.vectors):
            if vector:
                self.queue.append((index, 0))

    def next(self):

        if self.queue:
            # popleft curr vector and curr element index
            curr_vector_index, curr_element_index = self.queue.popleft()
            # how do we handle adding it into queue
            # this means there are still elements left
            if len(self.vectors[curr_vector_index]) > curr_element_index + 1:
                self.queue.append((curr_vector_index, curr_element_index + 1))
            return self.vectors[curr_vector_index][curr_element_index]
        raise StopIteration("No more elements to iterate")

    def hasNext(self):
        return len(self.queue) > 0