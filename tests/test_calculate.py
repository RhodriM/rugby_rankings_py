import unittest

import rugby_rankings.ratings_input
import rugby_rankings.ratings_output
import rugby_rankings.calculate
import rugby_rankings.weighting_high_score


class TestCalculate(unittest.TestCase):

    def test_set_pre_match_ratings(self):
        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)
        calc = rugby_rankings.calculate.Calculate(empty_input)

        calc._set_pre_match_ratings(0, 90.3)
        self.assertEqual(3.0, calc._team_a_pre_match_rating)
        self.assertEqual(90.3, calc._team_b_pre_match_rating)

        calc._set_pre_match_ratings(-4, 101)
        self.assertEqual(3.0, calc._team_a_pre_match_rating)
        self.assertEqual(100, calc._team_b_pre_match_rating)

        calc._set_pre_match_ratings(99.5, -5)
        self.assertEqual(100, calc._team_a_pre_match_rating)
        self.assertEqual(0, calc._team_b_pre_match_rating)

    def test_set_ratings_gap(self):
        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)
        calc = rugby_rankings.calculate.Calculate(empty_input)

        calc._set_pre_match_ratings(80, 90)
        calc._set_ratings_gap()
        self.assertAlmostEqual(7, calc._ratings_gap)

        calc._set_pre_match_ratings(40, 43)
        calc._set_ratings_gap()
        self.assertAlmostEqual(0, calc._ratings_gap)

        calc._set_pre_match_ratings(0, 90.3)
        calc._set_ratings_gap()
        self.assertAlmostEqual(10, calc._ratings_gap)

    def test_set_exchange(self):
        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)
        calc = rugby_rankings.calculate.Calculate(empty_input)

        calc._set_exchange()

        self.assertTrue(isinstance(calc._exchange, rugby_rankings.exchange.Exchange))

    def test_get_output(self):

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 5, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(78, r_output.get_team_a_rating())
        self.assertEqual(79, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 16, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(78.5, r_output.get_team_a_rating())
        self.assertEqual(78.5, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 0, 5)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(76, r_output.get_team_a_rating())
        self.assertEqual(81, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 0, 16)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(75.5, r_output.get_team_a_rating())
        self.assertEqual(81.5, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 0, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(77, r_output.get_team_a_rating())
        self.assertEqual(80, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(75, 80, 0, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(75.2, r_output.get_team_a_rating())
        self.assertEqual(79.8, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(75, 80, 0, 0, False, True)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(75.4, r_output.get_team_a_rating())
        self.assertEqual(79.6, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(80, 80, 0, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(79.70, r_output.get_team_a_rating())
        self.assertEqual(80.30, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(80, 80, 3, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(80.70, r_output.get_team_a_rating())
        self.assertEqual(79.30, r_output.get_team_b_rating())

        r_input = rugby_rankings.ratings_input.RatingsInput(77, 80, 3, 0)
        calc = rugby_rankings.calculate.Calculate(r_input)

        r_output = calc.get_output()
        self.assertEqual(78, r_output.get_team_a_rating())
        self.assertEqual(79, r_output.get_team_b_rating())