"""
WeightingWorldCup class
"""

import rugby_rankings.weighting


class WeightingWorldCup(rugby_rankings.weighting.Weighting):
    """
    WeightingWorldCup is a simple class just to apply a different multiplier
    for RWC games.
    """

    _multiplier = 2
