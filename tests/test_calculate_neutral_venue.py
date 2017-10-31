import unittest

import rugby_rankings.ratings_input
import rugby_rankings.ratings_output
import rugby_rankings.calculate_neutral_venue
import rugby_rankings.weighting_high_score


class TestCalculateNeutralVenue(unittest.TestCase):

    def test_set_pre_match_ratings(self):
        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)
        calc = rugby_rankings.calculate_neutral_venue.CalculateNeutralVenue(empty_input)

        calc._set_pre_match_ratings(0, 90.3)
        self.assertEqual(0.0, calc._team_a_pre_match_rating)
        self.assertEqual(90.3, calc._team_b_pre_match_rating)

        calc._set_pre_match_ratings(-4, 101)
        self.assertEqual(0.0, calc._team_a_pre_match_rating)
        self.assertEqual(100, calc._team_b_pre_match_rating)

        calc._set_pre_match_ratings(99.5, -5)
        self.assertEqual(99.5, calc._team_a_pre_match_rating)
        self.assertEqual(0, calc._team_b_pre_match_rating)