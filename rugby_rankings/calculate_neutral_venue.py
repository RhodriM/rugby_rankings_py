"""
CalculateNeutralVenue class: see below
"""

import rugby_rankings.calculate


class CalculateNeutralVenue(rugby_rankings.calculate.Calculate):
    """
    This class extends Calculate and overrides _set_pre_match_ratings to
    not give a home advantage.
    """

    def _set_pre_match_ratings(self, team_a_rating, team_b_rating):
        """
        Overrides Calculate's _set_pre_match_ratings to not give a home advantage.
        Imposes a minimum of 0 and maximum of 100 on pre-match ratings.

        :param team_a_rating: (float)
        :param team_b_rating: (float)
        :return: None
        """

        # ensure > 0
        team_a_rating = max(team_a_rating, 0)
        team_b_rating = max(team_b_rating, 0)

        self._team_a_pre_match_rating = min(team_a_rating, 100)
        self._team_b_pre_match_rating = min(team_b_rating, 100)
