from collections import deque


class XToY:

    def minimumNumberOfOperations(self, x: int, y: int) -> int:
        """
        Approach: BFS Queue
        T: O(N)
        S: O(N)
        :param x:
        :param y:
        :return:
        """

        if y >= x:
            return y - x

        seen = {x}
        queue = deque([(0, x)])
        

        while queue:
            k, n = queue.popleft()

            if y == n:
                return k

            if n % 11 == 0 and n // 11 not in seen:
                queue.append((k + 1, n // 11))
                seen.add(n // 11)
            if n % 5 == 0 and n // 5 not in seen:
                queue.append((k + 1, n // 5))
                seen.add(n // 5)
            if n - 1 not in seen:
                queue.append((k + 1, n - 1))
                seen.add(n - 1)
            if n + 1 not in seen:
                queue.append((k + 1, n + 1))
                seen.add(n + 1)


if __name__ == "__main__":
    xToY = XToY()
    print(xToY.minimumNumberOfOperations(26, 1))
