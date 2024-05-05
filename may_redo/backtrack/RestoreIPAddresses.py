from typing import List


class IPAddresses:

    def restore(self, s: str) -> List[str]:
        """
        Approach: BackTracking
        T: O(M^N * N)
        S: O(M * N)
        :param s:
        :return:
        """
        def backtrack(pos: int, octets: List[str]):

            # base
            if len(octets) == 4 and pos == len(s):
                ips.append(".".join(octets))
                return

            for size in range(1, 4):
                octet = s[pos: pos + size]
                if len(octet) > 1 and (octet[0] == '0' or int(octet) > 255):
                    continue
                if len(octet) < 4 and pos + size < len(s) + 1:
                    octets.append(octet)
                    backtrack(pos + size, octets)
                    octets.pop()

        ips = []
        backtrack(0, [])
        return ips
