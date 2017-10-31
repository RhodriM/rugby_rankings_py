"""
Main class - main entry point for package
"""

from rugby_rankings.calculate_neutral_venue import CalculateNeutralVenue
from rugby_rankings.calculate import Calculate
from rugby_rankings.ratings_input import RatingsInput


class Main(object):
    """
    Main class for accepting input, kicking off calculations and returning output.

    To use, instantiate(pass in RatingsInput) then call calculate() to get results.

    Attributes:

        _ratings_input: (RatingsInput) input object passed in that holds the
                        rankings and scores we need.
    """

    _ratings_input = None

    def __init__(self, r_input: RatingsInput):
        """

        :param r_input: (RatingsInput) input object containing all needed user input
        """
        self._ratings_input = r_input

    def calculate(self):
        """
        Determines if neutral venue and runs appropriate Calculate.get_output()

        :return: (RatingsOutput) represents new rankings
        """
        if self._ratings_input.is_neutral_venue:
            calc = CalculateNeutralVenue(self._ratings_input)
            return calc.get_output()

        calc = Calculate(self._ratings_input)
        return calc.get_output()
