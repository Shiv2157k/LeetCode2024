from typing import List


class RestoreIPAddress:

    def restore(self, s: str) -> List[str]:
        """
        Approach: Backtrack
        T: O(M^N * N)
        S: O(M * N)
        :param s:
        :return:
        """

        def backtrack(pos: int, octets: List[str]):

            # base case
            if pos == len(s) and len(octets) == 4:
                ips.append('.'.join(octets))
                return

            for size in range(1, 4):
                octet = s[size: size + pos]

                if len(octet) > 1 and (octet[0] == '0' or int(octet) > 255):
                    continue

                if len(octet) == 4 and pos + size < len(s) + 1:
                    octets.append(octet)
                    backtrack(pos + size, octets)
                    octets.pop()

        ips = []
        backtrack(0, [])
        return ips
