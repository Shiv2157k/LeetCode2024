from threading import Lock


class ListNode:

    def __init__(self, val: int = -1, next_node=None):
        self.val = val
        self.next = next_node


class CircularQueueV1:

    def __init__(self, k: int):
        self._head = None
        self._tail = None
        self._count = 0
        self._capacity = k

    def en_queue(self, value) -> bool:
        if self._count == self._capacity:
            return False
        if self._count == 0:
            self._head = ListNode(value)
            self._tail = self._head
        else:
            new_node = ListNode(value)
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1
        return True

    def de_queue(self) -> bool:
        if self._count == 0:
            return False
        self._head = self._head.next
        self._count -= 1
        return True

    def front(self) -> int:
        if self._count == 0:
            return -1
        return self._head.val

    def rear(self) -> int:
        if self._count == 0:
            return -1
        return self._tail.val

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._capacity


class CircularQueueV0:

    def __init__(self, k: int):
        self._queue = [0] * k
        self._head_index = 0
        self._count = 0
        self._capacity = k
        # for tail we calculate like below
        # (head_index + count) % capacity
        self._queue_lock = Lock()

    def en_queue(self, value) -> bool:
        with self._queue_lock:
            if self._count == self._capacity:
                return False
            self._queue[(self._head_index + self._count) % self._capacity] = value
            self._count += 1
        return True

    def de_queue(self) -> bool:
        with self._queue_lock:
            if self._count == 0:
                return False
            self._head_index = (self._head_index + 1) % self._capacity
            self._count -= 1
        return True

    def front(self) -> int:
        if self._count == 0:
            return -1
        return self._queue[self._head_index]

    def rear(self) -> int:
        if self._count == 0:
            return -1
        return self._queue[(self._head_index + self._count - 1) % self._capacity]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._capacity


if __name__ == "__main__":
    circular_queue_v0 = CircularQueueV0(5)
    print(circular_queue_v0.is_full())
    print(circular_queue_v0.is_empty())
    print(circular_queue_v0.en_queue(9))
    print(circular_queue_v0.en_queue(7))
    print(circular_queue_v0.en_queue(5))
    print(circular_queue_v0.en_queue(2))
    print(circular_queue_v0.de_queue())
    print(circular_queue_v0.en_queue(11))
    print(circular_queue_v0.front())
    print(circular_queue_v0.front())
    print(circular_queue_v0.rear())
    print(circular_queue_v0.is_full())
    print(circular_queue_v0.is_empty())

    print("-------****--------")

    circular_queue_v1 = CircularQueueV1(5)
    print(circular_queue_v1.is_full())
    print(circular_queue_v1.is_empty())
    print(circular_queue_v1.en_queue(9))
    print(circular_queue_v1.en_queue(7))
    print(circular_queue_v1.en_queue(5))
    print(circular_queue_v1.en_queue(2))
    print(circular_queue_v1.de_queue())
    print(circular_queue_v1.en_queue(11))
    print(circular_queue_v1.front())
    print(circular_queue_v1.front())
    print(circular_queue_v1.rear())
    print(circular_queue_v1.is_full())
    print(circular_queue_v1.is_empty())