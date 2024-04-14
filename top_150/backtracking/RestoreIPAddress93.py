from typing import List


class IPAddress:

    def restore(self, s: str) -> List[str]:
        """
        Approach: Back Tracking
        T: O(M^N * N)
        S: O(M * N)
        :param s:
        :return:
        """
        ips = []

        def backtrack(start: int, octets: List[str]):

            # base case
            if len(octets) == 4 and start == len(s):
                ips.append(".".join(octets))

            for size in range(1, 4):
                octet = s[start: start + size]
                # validation
                if len(octet) > 1 and (octet[0] == "0" or int(octet) > 255):
                    continue
                if len(octet) < 4 and start + size < len(s) + 1:
                    octets.append(octet)
                    backtrack(start + size, octets)
                    octets.pop()

        backtrack(0, [])
        return ips


if __name__ == "__main__":
    ipAddress = IPAddress()
    print(ipAddress.restore("0000"))
    print(ipAddress.restore("25525511135"))
    print(ipAddress.restore("101023"))
