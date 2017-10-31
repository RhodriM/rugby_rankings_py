import unittest

import rugby_rankings.main
import rugby_rankings.ratings_output

class TestMain(unittest.TestCase):

    def test_main(self):

        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0)
        rankings = rugby_rankings.main.Main(empty_input)

        self.assertTrue(isinstance(rankings.calculate(), rugby_rankings.ratings_output.RatingsOutput))

        empty_input = rugby_rankings.ratings_input.RatingsInput(0.0, 0.0, 0, 0, True)
        rankings = rugby_rankings.main.Main(empty_input)

        self.assertTrue(isinstance(rankings.calculate(), rugby_rankings.ratings_output.RatingsOutput))
