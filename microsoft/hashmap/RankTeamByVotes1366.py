from typing import List


class RankTeams:

    def byVotes(self, votes: List[str]) -> str:
        """
        Approach: HashMap and Sorting -> Bubble Sort
        T: O(S * log(S) * N)
        S: O(N)
        :param votes:
        :return:
        """

        if not votes:
            return ''

        totalVotes = len(votes[0])
        # build a hashmap with team member and list to store votes
        # Key - member | Val - list with totalVotes size
        memberScore = {}
        for member in votes[0]:
            memberScore[member] = [0] * totalVotes

        # add the votes for each member
        for vote in votes:
            for rank, member in enumerate(list(vote)):
                memberScore[member][rank] += 1

        # to handle ties add the member at the end
        for member, scores in memberScore.items():
            scores.append(-ord(member))

        # need to sort one way is using in built functions
        # members = sorted(memberScore, key=memberScore.get, reverse=True)
        # return ''.join(members)

        # bubble sort
        teams = list(memberScore.keys())
        for i in range(len(teams)):
            for j in range(len(teams) - i - 1):
                if tuple(memberScore[teams[j]] + [teams[j]]) < tuple(memberScore[teams[j + 1]] + [teams[j + 1]]):
                    teams[j], teams[j + 1] = teams[j + 1], teams[j]
        return ''.join(teams)
