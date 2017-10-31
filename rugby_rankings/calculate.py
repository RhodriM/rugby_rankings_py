"""
Calculate Class
"""

import rugby_rankings.ratings_input
import rugby_rankings.ratings_output
import rugby_rankings.match_result
import rugby_rankings.exchange
import rugby_rankings.weighting_world_cup
import rugby_rankings.weighting_high_score


class Calculate(object):
    """
    Class for calculating the new Ranking points for the teams in question.

    After construction, get_output() will return a RatingsOutput instance
    containing new rankings.

    Attributes:
        _team_a_pre_match_rating: adjusted pre-match rating for team A to
                                be used in the calculation.
                                This is after taking into account home advantage etc.
        _team_b_pre_match_rating: adjusted pre-match rating for team B to
                                be used in the calculation.
                                This is after taking into account home advantage etc.
        _ratings_gap: The ratings Gap between the two teams
                    (after home advantage etc adjustments)
        _ratings_output: The RatingsOutput instance containing new ranking
                    scores.
        _exchange: Instance of Exchange for calculating the points exchange between
                    the two teams.
        _ratings_input: The supplied input instance.
        _match_result: Supplied instance of MatchResult.

    Constants:
        HOME_TEAM_ADVANTAGE: How many points to add to the home team's ranking
                            points before calculation.
        MAX_RATINGS_GAP: Default 10.
    """

    _team_a_pre_match_rating = None
    _team_b_pre_match_rating = None
    _ratings_gap = None
    _ratings_output = None
    _exchange = None
    _ratings_input = None
    _match_result = None

    HOME_TEAM_ADVANTAGE = 3.0
    MAX_RATINGS_GAP = 10

    def __init__(self, ratings_input: rugby_rankings.ratings_input.RatingsInput):
        """
        Determines adjusted pre-match rankings and sets rating gap accordingly.

        :param ratings_input: (RatingsInput)
        """

        # set adjusted pre match ranking points
        self._set_pre_match_ratings(
            ratings_input.get_rounded_team_a_rating(),
            ratings_input.get_rounded_team_b_rating()
        )

        self._ratings_input = ratings_input

        self._match_result = rugby_rankings.match_result.MatchResult(
            self._team_a_pre_match_rating,
            self._team_b_pre_match_rating,
            ratings_input.team_a_score,
            ratings_input.team_b_score
        )

        # determine ratings gap
        self._set_ratings_gap()

    def _set_pre_match_ratings(self, team_a_rating, team_b_rating):
        """
        Sets adjusted pre-match ratings: home team gets self.HOME_TEAM_ADVANTAGE
        added and both teams ratings are min/maxed at 0/100.

        :param team_a_rating: (float)
        :param team_b_rating: (float)
        :return: None
        """

        # ensure > 0
        team_a_rating = max(team_a_rating, 0)
        team_b_rating = max(team_b_rating, 0)

        # add home advantage
        team_a_rating = team_a_rating + self.HOME_TEAM_ADVANTAGE

        # max points 100
        self._team_a_pre_match_rating = min(team_a_rating, 100)
        self._team_b_pre_match_rating = min(team_b_rating, 100)

    def _set_ratings_gap(self):
        """
        Sets rating gap: higher rating minus lower, but only up to
        self.MAX_RATINGS_GAP

        :return: None
        """
        ratings_gap = abs(self._team_a_pre_match_rating - self._team_b_pre_match_rating)

        self._ratings_gap = min(ratings_gap, self.MAX_RATINGS_GAP)

    def _set_exchange(self):
        """
        Creates new Exchange instance for calculating Exchange amount; passing
        in any relevant weightings.

        :return: None
        """

        # create weightings

        high_score = rugby_rankings.weighting_high_score.WeightingHighScore(
            self._ratings_input.team_a_score,
            self._ratings_input.team_b_score)

        weightings = [high_score]

        if self._ratings_input.is_rugby_world_cup:
            world_cup = rugby_rankings.weighting_world_cup.WeightingWorldCup(
                self._ratings_input.team_a_score,
                self._ratings_input.team_b_score)

            weightings.append(world_cup)

        self._exchange = rugby_rankings.exchange.Exchange(
            self._ratings_gap,
            self._match_result,
            weightings
        )

    def get_output(self):
        """
        Calls exchange.calculate(), passes back results as RatingsOutput instance.

        :return: (RatingsOutput)
        """

        r_output = rugby_rankings.ratings_output.RatingsOutput()

        self._set_exchange()

        self._exchange.calculate()

        r_output.set_team_a_rating(self._get_new_team_rating('A'))
        r_output.set_team_b_rating(self._get_new_team_rating('B'))

        return r_output

    def _get_new_team_rating(self, team):
        """
        Given a team ('A'/'B'), determines new team rating.

        :param team: (string) Should be 'A' or 'B' (unless extended in future)
        :return: (float) the team's new rating
        """

        # a function we can use for different team inputs
        input_rating_function = getattr(
            self._ratings_input,
            'get_rounded_team_' + team.lower() + '_rating'
        )

        if self._match_result.higher_team == rugby_rankings.match_result.MatchResult.TEAMS_EQUAL:
            # teams rankings points equal before game

            if self._match_result.result == rugby_rankings.match_result.MatchResult.DRAW:
                # no change
                return input_rating_function()

            if self._match_result.result == team:
                # this team wins and gets points increase
                return input_rating_function() + self._exchange.exchange_amount

            # else team lost
            return input_rating_function() - self._exchange.exchange_amount

        if self._match_result.higher_team == team:
            # team in question is ranked higher before game

            if self._match_result.result == team:
                # team won
                return input_rating_function() + self._exchange.exchange_amount

            # team lost or drew, as they're higher ranked they lose points
            return input_rating_function() - self._exchange.exchange_amount

        # if we get here we're dealing with lower-ranked team before game

        if (self._match_result.result == team
                or self._match_result.result == rugby_rankings.match_result.MatchResult.DRAW):

            # lower ranked team gets points from win or draw
            return input_rating_function() + self._exchange.exchange_amount

        # lower ranked team lost
        return input_rating_function() - self._exchange.exchange_amount
