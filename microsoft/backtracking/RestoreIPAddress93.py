from typing import List


class RestoreIpAddress:

    def restoreIPAddresses(self, s: str) -> List[str]:
        def backtrack(pointer: int, octets: List[str]):

            # base case
            if len(octets) == 4 and pointer == len(s):
                ips.append(".".join(octets))
                return

            for size in range(1, 4):
                octet = s[pointer: pointer + size]

                if len(octet) > 1 and (octet[0] == '0' or int(octet) > 255):
                    continue

                if len(octet) < 4 and pointer + size < len(s) + 1:
                    octets.append(octet)
                    backtrack(pointer + size, octets)
                    octets.pop()

        backtrack(0, [])
        ips = []
        return ips
