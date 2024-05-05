from typing import List, Dict


class RankTeamByVotes:

    def rank_teams(self, votes: List[str]) -> str:
        """
        Approach: HashMap and sort
        T: O(N * M)
        S: O(N * M)
        :param votes:
        :return:
        """

        if len(votes) == 0:
            return ''

        total_voters: int = len(votes[0])
        score: Dict[str, List[int]] = {}

        for member in votes[0]:
            score[member] = [0] * total_voters

        for vote in votes:
            for rank, member in enumerate(list(vote)):
                score[member][rank] += 1

        for member, vote in score.items():
            vote.append(-ord(member))

        teams = list(score.keys())

        for i in range(len(teams)):
            for j in range(0, len(teams) - i - 1):
                # if tuple(score[teams[j]] + [teams[j]]) < tuple(score[teams[j + 1] + teams[j + 1]]):
                if self.compare(score, teams[j], teams[j + 1]):
                    teams[j], teams[j + 1] = teams[j + 1], teams[j]
        # score = sorted(score, key=score.get, reverse=True)
        return ''.join(teams)

    def compare(self, score, team1, team2):
        # Custom comparison function to compare teams based on scores
        scores1 = score[team1]
        scores2 = score[team2]
        for i in range(len(scores1)):
            if scores1[i] != scores2[i]:
                return scores1[i] < scores2[i]  # Change to > for descending order
        # If scores are equal, use lexicographical comparison of team names
        return team1 > team2

