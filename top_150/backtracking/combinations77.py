from typing import List


class Combinations:

    def combineV1(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Back tracking optimized
        T: O(n! / (k - 1)! * (n - k)!)
        S: O(K)
        :param n:
        :param k:
        :return:
        """

        result = []

        def backtrack(num: int, path: List[int]) -> None:

            # base case
            if len(path) == k:
                result.append(list(path))
                return

            need = k - len(path)
            remain = n - num + 1
            available = remain - need

            for curr in range(num, num + available + 1):
                path.append(curr)
                backtrack(curr + 1, path)
                path.pop()
            return
        backtrack(1, [])
        return result

    def combineV0(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Back tracking
        T: O(n! / k! * (n - k)!)
        S: O(K)
        :param n:
        :param k:
        :return:
        """

        result = []

        def backtrack(num: int, path: List[int]) -> None:

            # base case
            if len(path) == k:
                result.append(list(path))
                return

            for nextNum in range(num, n + 1):
                path.append(nextNum)
                backtrack(nextNum + 1, path)
                path.pop()
        backtrack(1, [])
        return result


if __name__ == "__main__":
    combinations = Combinations()
    print(combinations.combineV0(4, 2))
    print(combinations.combineV0(4, 3))

    print(combinations.combineV1(4, 2))
    print(combinations.combineV1(4, 3))