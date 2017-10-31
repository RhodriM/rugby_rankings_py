"""
WeightingHighScore class
"""

import rugby_rankings.weighting


class WeightingHighScore(rugby_rankings.weighting.Weighting):
    """
    WeightingHighScore checks if team won by more than the 'HIGH_SCORE'
    (currently 15), and if so returns adjusted multiplier.

    Attributes:
        HIGH_SCORE (int): How much a team needs to win by more than to get
                          high score multiplier
        HIGH_SCORE_MULTIPLIER (float):
    """

    HIGH_SCORE = 15
    HIGH_SCORE_MULTIPLIER = 1.5

    def __init__(self, first_score, second_score):
        """
        Determines if score of match is enough to trigger High Score
        Multiplier, and if so overrides default multiplier(1) with high score
        multiplier.

        :param first_score: (int)
        :param second_score: (int)
        """
        super().__init__(first_score, second_score)
        if abs(first_score - second_score) > self.HIGH_SCORE:
            self._multiplier = self.HIGH_SCORE_MULTIPLIER
