from .building import Building

"""
The Strategy design pattern can be applied here since the system 
could have multiple dispatch request strategy classes. 
Therefore, depending on the particular layout of the building and its scenarios, 
we choose a set of dispatch request strategy classes.

We can also use the State and Delegation design pattern for this problem. 
Instead of implementing all methods on its own, 
the context object stores a reference to one of the state objects that represents 
its current state and delegates all the state-specific tasks to that object. 
For example, elevators have multiple states like working or idle, etc. 
Based on the state, 
the system infers which method or behavior of the elevator should be invoked.
"""


class __ElevatorSystem(object):
    __instances = None

    def __new__(cls, __ElevatorSystem=None):
        if cls.__instances is None:
            cls.__instances = super(__ElevatorSystem, cls).__new__(cls)
        return cls.__instances


class ElevatorSystem(metaclass=__ElevatorSystem):

    def __init__(self, building: Building):
        self.__building = Building

    def monitoring(self):
        pass

    def dispatcher(self):
        # can be implemented in following ways through scheduling algorithm
        # 1. FCFS - Queue to track which passenger comes first
        # First Come First Serve (FCFS) is a scheduling algorithm
        # by which the passenger who comes first gets the elevator car and reaches the destination.
        # There are four states of an elevator car with respect to the passenger:
        # - The elevator car is in an idle state.
        # - The elevator car is moving towards the passenger and in the same direction the passenger wants to go.
        # - An elevator car is moving towards the passenger but in the opposite direction the passenger wants to go.
        # - The elevator car is moving away from the passenger.
        # 2. Shortest Seek Time First(SSTF) - better then FCFS (Priority Queue, MinHeap, Array DS)
        # 3.SCAN - Elevator Algorithm - Two Bool Arrays, Single HashMap or Two Priority Queues
        # SCAN is also known as the Elevator Algorithm.
        # The elevator car starts from one end of the building and
        # moves towards the other end, servicing requests in between.
        # The advantage of this method is that it serves multiple requests in parallel.
        # However, it results in increased cost as the elevator car only changes its
        # direction at either the top floor, or the lowest floor.
        # 4. LOOK(Look Ahead SCAN Algorithm) - HashMap, TreeMap or Binary Search Tree
        # It is an improved version of the SCAN Algorithm.
        # In this algorithm, the elevator car stops when there is no request in front of them.
        # It will move again on the basis of the request.
        # The advantage of this algorithm is that the elevator car does not always
        # go till the end of the building but can change its direction in between.
        pass
