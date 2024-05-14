class IsomorphicStrings:

    def is_isomorphic(self, s: str, t: str) -> bool:
        """
        T: O(M + N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """
        def hash_index(string: str) -> str:

            index_map = {}
            hash_str = []

            for index, char in enumerate(string):
                if char not in index_map:
                    index_map[char] = index
                hash_str.append(str(index_map[char]))
            return ''.join(hash_str)

        hash_s = hash_index(s)
        hash_t = hash_index(t)
        return hash_s == hash_t
