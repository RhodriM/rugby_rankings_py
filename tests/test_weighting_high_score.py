import unittest

import rugby_rankings.weighting_high_score


class TestWeightingHighScore(unittest.TestCase):

    def test_high_score(self):

        weighting = rugby_rankings.weighting_high_score.WeightingHighScore(10, 15)
        self.assertEqual(1, weighting.apply(1))

        weighting = rugby_rankings.weighting_high_score.WeightingHighScore(15, 10)
        self.assertEqual(1, weighting.apply(1))

        weighting = rugby_rankings.weighting_high_score.WeightingHighScore(0, 15)
        self.assertEqual(1, weighting.apply(1))

        weighting = rugby_rankings.weighting_high_score.WeightingHighScore(0, 16)
        self.assertEqual(1.5, weighting.apply(1))

        weighting = rugby_rankings.weighting_high_score.WeightingHighScore(100, 84)
        self.assertEqual(1.5, weighting.apply(1))
