"""
Module containing RatingsInput class
"""


class RatingsInput(object):
    """
    Simple class for passing around inputs: initial team ratings, scores etc

    Attributes:
        _team_a_rating (float): team a initial rating. Prefer private/protected,
                                use get_rounded_team_a_rating()
        _team_b_rating (float): team b initial rating. Prefer private/protected,
                                use get_rounded_team_b_rating()
        team_a_score (int)
        team_b_score (int)
        is_neutral_venue (bool)
        is_rugby_world_cup (bool)

    """

    _team_a_rating = -1.0
    _team_b_rating = -1.0
    team_a_score = -1
    team_b_score = -1
    is_neutral_venue = False
    is_rugby_world_cup = False

    def __init__(self,
                 team_a_rating,
                 team_b_rating,
                 team_a_score,
                 team_b_score,
                 is_neutral_venue=False,
                 is_rugby_world_cup=False):
        """

        :param team_a_rating: (float) team a initial rating.
        :param team_b_rating: (float) team b initial rating.
        :param team_a_score: (int)
        :param team_b_score: (int)
        :param is_neutral_venue: (bool)
        :param is_rugby_world_cup: (bool)
        """
        self._team_a_rating = team_a_rating
        self._team_b_rating = team_b_rating
        self.team_a_score = team_a_score
        self.team_b_score = team_b_score
        self.is_neutral_venue = is_neutral_venue
        self.is_rugby_world_cup = is_rugby_world_cup

    def get_rounded_team_a_rating(self):
        """

        :return: (float) team a rating rounded to 2dp
        """
        return float("{0:.2f}".format(self._team_a_rating))

    def get_rounded_team_b_rating(self):
        """

        :return: (float) team b rating rounded to 2dp
        """
        return float("{0:.2f}".format(self._team_b_rating))
