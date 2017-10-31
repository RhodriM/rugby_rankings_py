import unittest

import rugby_rankings.ratings_input


class TestRatingsInput(unittest.TestCase):

    def test_construct(self):

        inputObj = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)

        self.assertTrue(
            isinstance(inputObj, rugby_rankings.ratings_input.RatingsInput)
        )

        inputObj = rugby_rankings.ratings_input.RatingsInput(
            0.0, 0.0, 0, 0, True, True
        )
        self.assertTrue(
            isinstance(inputObj, rugby_rankings.ratings_input.RatingsInput)
        )

    def test_types(self):
        inputObj = rugby_rankings.ratings_input.RatingsInput(
            1.111, 90.199, 3, 2.2
        )

        self.assertTrue(
            isinstance(inputObj.get_rounded_team_a_rating(), float)
        )

        self.assertEqual(inputObj.get_rounded_team_a_rating(), 1.11)

        self.assertEqual(inputObj.get_rounded_team_b_rating(), 90.20)

        inputObj = rugby_rankings.ratings_input.RatingsInput(
            1.111, 90.199, 3, 2.2, True, True
        )

        self.assertEqual(inputObj.is_rugby_world_cup, True)
        self.assertEqual(inputObj.is_neutral_venue, True)


if __name__ == "__main__":
    unittest.main()
