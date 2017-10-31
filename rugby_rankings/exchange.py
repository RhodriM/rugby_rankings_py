"""
Exchange class
"""

import rugby_rankings.match_result
import rugby_rankings.calculate
import rugby_rankings.invalid_match_result_exception


class Exchange(object):
    """
    Exchange class for calculating the points exchange between the two teams.

    Attributes:
        _ratings_gap: (float) gap in ratings between teams
        exchange_amount: (float) points exchange
        _match_result: (MatchResult) input MatchResult instance
        _weightings: (lst) list of Weighting instances, used for adjusting exchange_amount.

    Constants:
        BETTER_TEAM_WIN: 'B' Used for determining points exchange
        UNDERDOG_WIN: 'U' Used for determining points exchange
        DRAW: 'D' Used for determining points exchange
    """

    _ratings_gap = None
    exchange_amount = None
    _match_result = None
    _weightings = None

    BETTER_TEAM_WIN = 'B'
    UNDERDOG_WIN = 'U'
    DRAW = 'D'

    def __init__(
            self,
            ratings_gap,
            match_result: rugby_rankings.match_result.MatchResult,
            weightings=None):
        """
        Constructor takes 3 params: (adjusted) ratings gap between teams, a
        MatchResult instance and an array or Weightings instances that will be
        applied to the resulting exchange amount.

        :param ratings_gap: (float) adjusted ratings between teams
        :param match_result: (MatchResult) info on game played
        :param weightings: (lst) array of weightings for adjusting exchange amount. Can be None
        """

        self._ratings_gap = ratings_gap
        self._match_result = match_result

        if weightings is None:
            weightings = []

        self._weightings = weightings

    def calculate(self):
        """
        Calculates rating points exchange between teams and returns it.

        :return: (float) the points exchange
        :raises InvalidMatchResultException: if cannot determine match result
        """

        base = self._ratings_gap / rugby_rankings.calculate.Calculate.MAX_RATINGS_GAP

        if (self._match_result.is_underdog_win()
                or self._match_result.is_equals_win()):

            self.exchange_amount = 1 + base
            self._apply_weightings()
            return self.exchange_amount

        if self._match_result.is_higher_team_win():

            self.exchange_amount = 1 - base
            self._apply_weightings()
            return self.exchange_amount

        if self._match_result.result == rugby_rankings.match_result.MatchResult.DRAW:

            self.exchange_amount = base
            self._apply_weightings()
            return self.exchange_amount

        raise rugby_rankings.invalid_match_result_exception.InvalidMatchResultException(
            "invalid match result: " + self._match_result.result)

    def _apply_weightings(self):
        """
        Apply weightings to result.

        :return: None
        """

        for weighting in self._weightings:

            if not isinstance(weighting, rugby_rankings.weighting.Weighting):
                continue

            self.exchange_amount = weighting.apply(self.exchange_amount)
