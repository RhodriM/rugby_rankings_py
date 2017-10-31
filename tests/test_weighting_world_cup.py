import unittest

import rugby_rankings.weighting_world_cup


class TestWeightingWorldCup(unittest.TestCase):

    def test_world_cup(self):

        weighting = rugby_rankings.weighting_world_cup.WeightingWorldCup(10, 15)
        self.assertEqual(2, weighting.apply(1))

        weighting = rugby_rankings.weighting_world_cup.WeightingWorldCup(0, 16)
        self.assertEqual(2, weighting.apply(1))
