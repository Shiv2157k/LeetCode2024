from typing import List


class CodecV2:
    """
    Approach: Chunked Transfer Encoding
    T: O(N)
    S: O(K)
    """

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for s in strs:
            encodedString += str(len(s)) + '#' + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        while i < len(s):
            delim = s.find('#', i)
            length = int(s[i:delim])

            str_ = s[delim + 1: delim + 1 + length]
            decodedString.append(str_)
            i = delim + 1 + length
        return decodedString


class CodecV1:
    """
    Approach: Escaping
    T: O(N)
    S: O(K)
    """

    def encode(self, strs: List[str]) -> str:
        encodedString = ''

        for s in strs:
            encodedString += s.replace('/', '//') + '/:'
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        currentString = ''
        i = 0

        while i < len(s):

            if s[i: i + 2] == '/:':
                decodedString.append(currentString)
                currentString = ''
                i += 2
            elif s[i: i + 2] == '//':
                currentString += '/'
                i += 2
            else:
                currentString += s[i]
                i += 1
        return decodedString


class CodecV0:
    """
    Approach: Non ASCII Delimeter
    T: O(N)
    S: O(K)
    """

    def encode(self, strs: List[str]) -> str:
        return "😁".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("😁")


if __name__ == "__main__":
    codecV0 = CodecV0()
    print(codecV0.encode(["Hello", "World"]))
    print(codecV0.decode("HelloWorld"))

    codecV1 = CodecV1()
    print(codecV1.encode(["Hello/", "World/:"]))
    print(codecV1.decode("Hello///:World//:/:"))

    codecV2 = CodecV2()
    print(codecV2.encode(["Hello#", "World/:"]))
    print(codecV2.decode("6#Hello#7#World/:"))
