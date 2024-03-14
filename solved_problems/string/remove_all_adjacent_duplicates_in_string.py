

class String:

    def remove_k_adj_dup(self, s: str, k: int):
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        stack = []
        for char in s:
            # if stack has data and char matches with stack top val
            if stack and char == stack[-1][0]:
                # increment the counter
                stack[-1][1] += 1
                # if it exceeds or equals to k pop the stack
                if stack[-1][1] >= k:
                    stack.pop()
            else:  # store the nonadjacent k values
                stack.append([char, 1])

        # build the string
        res = ''
        for char, count in stack:
            res += char * count
        return res


if __name__ == "__main__":
    string = String()
    print(string.remove_k_adj_dup("deeedbbcccbdaa", 3))
    print(string.remove_k_adj_dup("pbbcggttciiippooaais", 2))
    print(string.remove_k_adj_dup("pbbcggtttciiippooaais", 3))