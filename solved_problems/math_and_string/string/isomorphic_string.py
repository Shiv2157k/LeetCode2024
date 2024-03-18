class Isomorphic:

    def _transform_string(self, string: str) -> str:
        index_map = {}
        transform_str = []

        for index, char in enumerate(string):
            if char not in index_map:
                index_map[char] = index
            transform_str.append(str(index_map[char]))
        return " ".join(transform_str)

    def is_isomorphic_string_v1(self, s: str, t: str) -> bool:
        """
        Approach: Translating index as string using HashMap
        T: O(N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """
        return self._transform_string(s) == self._transform_string(t)

    def is_isomorphic_string_v0(self, s: str, t: str) -> bool:
        """
        Approach: Hash Map
        T: O(N)
        S: O(1)
        :param s:
        :param t:
        :return:
        """
        map_s_t, map_t_s = {}, {}

        for char1, char2 in zip(s, t):

            if char1 not in map_s_t and char2 not in map_t_s:
                map_s_t[char1] = char2
                map_t_s[char2] = char1
            elif map_s_t[char1] != char2 or map_t_s[char2] != char1:
                return False
        return True


if __name__ == '__main__':
    isomorphic = Isomorphic()
    print(isomorphic.is_isomorphic_string_v1("add", "egg"))
    print(isomorphic.is_isomorphic_string_v0("add", "egg"))

    print(isomorphic.is_isomorphic_string_v1("foo", "bar"))
    print(isomorphic.is_isomorphic_string_v0("foo", "bar"))

    print(isomorphic.is_isomorphic_string_v1("paper", "title"))
    print(isomorphic.is_isomorphic_string_v0("paper", "title"))
