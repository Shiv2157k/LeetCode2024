from typing import List, Dict


class RankTeamByVotes:

    def rank_teams(self, votes: List[str]) -> str:
        """
        Approach: HashMap and sort
        T: O(N * M + N^2)
        S: O(N * M + N^2)
        :param votes:
        :return:
        """

        if len(votes) == 0:
            return ''

        total_voters = len(votes[0])
        score: Dict[str, List[int]] = {}

        for member in votes[0]:
            score[member] = [0] * total_voters

        for vote in votes:
            for rank, member in enumerate(list(vote)):
                score[member][rank] += 1

        # add sentinel
        for member, vote in score.items():
            vote.append(-ord(member))

        teams = list(score.keys())

        for i in range(len(teams)):
            for j in range(0, len(teams) - i - 1):

                if self.__compare(score, teams[j], teams[j + 1]):
                    teams[j], teams[j + 1] = teams[j + 1], teams[j]
        return ''.join(teams)

    def __compare(self, score, team1, team2):

        score1 = score[team1]
        score2 = score1[team2]

        for i in range(len(score1)):
            if score1[i] != score2[i]:
                return score1[i] < score2[i]
        return team1 > team2
