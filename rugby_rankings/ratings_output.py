"""
Module containing RatingsOutput class
"""


class RatingsOutput(object):
    """
    RatingsOutput class - simple class, just to return the new team ranking
    points after the game.

    Attributes:
        _team_a_rating (float): New Team A ranking points.
                                Prefer private/protected, use get and set
                                methods to ensure rounded etc
        _team_b_rating (float): New Team B ranking points.
                                Prefer private/protected, use get and set
                                methods to ensure rounded etc
    """
    _team_a_rating = 0.0
    _team_b_rating = 0.0

    def get_team_a_rating(self):
        """

        :return: float
        """
        return float(self._team_a_rating)

    def get_team_b_rating(self):
        """

        :return: float
        """
        return float(self._team_b_rating)

    def set_team_a_rating(self, team_a_rating):
        """
        Sets team_a_rating within min/max bounds, also rounds to 2dp
        :param team_a_rating: float
        :return:
        """
        team_a_rating = max(min(100, team_a_rating), 0)
        self._team_a_rating = float("{0:.2f}".format(team_a_rating))

    def set_team_b_rating(self, team_b_rating):
        """
        Sets team_b_rating within min/max bounds, also rounds to 2dp
        :param team_b_rating: float
        :return:
        """
        team_b_rating = max(min(100, team_b_rating), 0)
        self._team_b_rating = float("{0:.2f}".format(team_b_rating))
