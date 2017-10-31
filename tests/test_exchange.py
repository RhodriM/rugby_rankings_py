import unittest

import rugby_rankings.exchange
import rugby_rankings.match_result
import rugby_rankings.weighting_high_score
import rugby_rankings.weighting_world_cup


class TestExchange(unittest.TestCase):

    def test_calculate(self):

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result)
        self.assertAlmostEqual(0.3, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result)
        self.assertAlmostEqual(0, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result)
        self.assertAlmostEqual(1, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result)
        self.assertAlmostEqual(0.7, exc.calculate())

    def test_weighting_high_score(self):

        high_score = rugby_rankings.weighting_high_score.WeightingHighScore(17, 0)
        weightings = [high_score]

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(0.45, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(0, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(1.5, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(1.05, exc.calculate())

    def test_weighting_world_cup(self):

        world_cup = rugby_rankings.weighting_world_cup.WeightingWorldCup(17, 0)
        weightings = [world_cup]

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(0.6, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(0, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(2, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(1.4, exc.calculate())

    def test_weighting_high_score_and_world_cup(self):

        world_cup = rugby_rankings.weighting_world_cup.WeightingWorldCup(17, 0)
        high_score = rugby_rankings.weighting_high_score.WeightingHighScore(17, 0)
        weightings = [world_cup, high_score]

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(0.9, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 0, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(0, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(0, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(0, match_result, weightings)
        self.assertAlmostEqual(3, exc.calculate())

        match_result = rugby_rankings.match_result.MatchResult(3, 0, 7, 0)
        exc = rugby_rankings.exchange.Exchange(3, match_result, weightings)
        self.assertAlmostEqual(2.10, exc.calculate())