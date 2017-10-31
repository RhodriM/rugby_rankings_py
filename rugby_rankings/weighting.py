"""
Abstract Weighting class
"""

from abc import ABCMeta


class Weighting():
    """
    Base Weighting class. Weighting classes passed to Exchange to adjust final
    exchange points amount. This base class just has a multiplier of 1, ie does
    not affect exchange points.
    Attributes:
        _multiplier (float): multiplier to adjust exchange amount
    """

    __metaclass__ = ABCMeta
    _multiplier = 1.0

    def __init__(self, first_score, second_score):
        """

        :param first_score:
        :param second_score:
        """
        pass

    def apply(self, points):
        """
        Apply weighting to score and return

        :param points: (float)
        :return: (float)
        """
        return points * self._multiplier
