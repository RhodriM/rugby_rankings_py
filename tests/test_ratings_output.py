import unittest

import rugby_rankings.ratings_output


class TestRatingsOutput(unittest.TestCase):

    def test_output(self):

        test_output_ratings = rugby_rankings.ratings_output.RatingsOutput()
        test_output_ratings.set_team_a_rating(0)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_a_rating(), float)
        )
        self.assertEqual(
            0.0, test_output_ratings.get_team_a_rating()
        )

        test_output_ratings.set_team_b_rating(100)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_b_rating(), float)
        )
        self.assertEqual(
            100.0, test_output_ratings.get_team_b_rating()
        )

        test_output_ratings.set_team_a_rating(-1)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_a_rating(), float)
        )
        self.assertEqual(
            0.0, test_output_ratings.get_team_a_rating()
        )

        test_output_ratings.set_team_b_rating(101)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_b_rating(), float)
        )
        self.assertEqual(
            100.0, test_output_ratings.get_team_b_rating()
        )

        test_output_ratings.set_team_a_rating(99999999999999999999999)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_a_rating(), float)
        )
        self.assertEqual(
            100.0, test_output_ratings.get_team_a_rating()
        )

        test_output_ratings.set_team_b_rating(34.246563)
        self.assertTrue(
            isinstance(test_output_ratings.get_team_b_rating(), float)
        )
        self.assertEqual(
            34.25, test_output_ratings.get_team_b_rating()
        )
