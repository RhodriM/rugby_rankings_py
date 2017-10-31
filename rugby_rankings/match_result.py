"""
MatchResult class
"""


class MatchResult(object):
    """
    Represents a MatchResult and holds properties such as which was the higher
    ranked team before the match, who won etc.

    Properties:
        _result: (string) Which team won - or drew.
        _higher_team: (string) who was higher ranked team before game?

    Attributes:

        TEAM_A_WIN: (string) constant for _result team a won
        TEAM_B_WIN: (string) constant for _result team b won
        DRAW: (string) constant for _result draw

        HIGHER_A: (string) team a was higher ranked before game
        HIGHER_B: (string) team b was higher ranked before game
        TEAMS_EQUAL: (string) teams were equally ranked
    """

    TEAM_A_WIN = 'A'
    TEAM_B_WIN = 'B'
    DRAW = 'D'

    HIGHER_A = 'A'
    HIGHER_B = 'B'
    TEAMS_EQUAL = 'E'

    def __init__(self,
                 team_a_adjusted_rating,
                 team_b_adjusted_rating,
                 team_a_score,
                 team_b_score):
        """

        :param team_a_adjusted_rating: float
        :param team_b_adjusted_rating: float
        :param team_a_score: int
        :param team_b_score: int
        """

        self.higher_team = (team_a_adjusted_rating, team_b_adjusted_rating)
        self.result = (team_a_score, team_b_score)

    @property
    def higher_team(self):
        """
        Which team won - or drew.
        :return: str
        """
        return self._higher_team

    @higher_team.setter
    def higher_team(self, value):
        """
        Determines which (if either) team was higher ranked before game.

        :param value: tuple of team_a_rating and team_b_rating (both floats)
        :return: None
        """

        team_a_rating, team_b_rating = value

        # you try to do things the python way and it complains
        # (and all I really wanted was a setter and getter)
        # pylint: disable=attribute-defined-outside-init

        if team_a_rating == team_b_rating:
            self._higher_team = self.TEAMS_EQUAL
            return

        self._higher_team = \
            self.HIGHER_A if team_a_rating > team_b_rating else self.HIGHER_B

    @property
    def result(self):
        """
        who was higher ranked team before game?
        :return: str
        """
        return self._result

    @result.setter
    def result(self, value):
        """
        Determines which team (if either) won.

        :param value: tuple of team_a_score, team_b_score (both ints)
        :return: None
        """

        team_a_score, team_b_score = value

        # pylint: disable=attribute-defined-outside-init

        if team_a_score == team_b_score:
            self._result = self.DRAW
            return

        self._result =\
            self.TEAM_A_WIN if team_a_score > team_b_score else self.TEAM_B_WIN

    def is_underdog_win(self):
        """
        Did the lower ranked team win?
        Also returns false if there was no higher team.

        :return: bool
        """

        if (self._result != self.DRAW
                and not self.is_equals_win()
                and self._result != self._higher_team):
            return True

        return False

    def is_higher_team_win(self):
        """
        Did the higher ranked team win?
        Also returns false if no higher team.

        :return: bool
        """
        if (self._result != self.DRAW
                and not self.is_equals_win()
                and self._result == self._higher_team):
            return True

        return False

    def is_equals_win(self):
        """
        Was there a win when the two teams were equally ranked?

        :return: bool
        """
        if (self._result != self.DRAW
                and self._higher_team == self.TEAMS_EQUAL):
            return True

        return False
