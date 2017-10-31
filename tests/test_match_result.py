import unittest

import rugby_rankings.match_result


class TestMatchResult(unittest.TestCase):

    def test_match_result_draw(self):

        match_result_obj = rugby_rankings.match_result.MatchResult(0, 0, 0, 0)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.TEAMS_EQUAL,
            match_result_obj.higher_team
        )

        self.assertFalse(match_result_obj.is_higher_team_win())
        self.assertFalse(match_result_obj.is_underdog_win())
        self.assertFalse(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.DRAW,
            match_result_obj.result
        )

        match_result_obj = rugby_rankings.match_result.MatchResult(3, 0, 0, 0)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.HIGHER_A,
            match_result_obj.higher_team
        )

        self.assertFalse(match_result_obj.is_higher_team_win())
        self.assertFalse(match_result_obj.is_underdog_win())
        self.assertFalse(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.DRAW,
            match_result_obj.result
        )

    def test_match_result_team_a_win(self):
        match_result_obj = rugby_rankings.match_result.MatchResult(0, 0, 3, 0)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.TEAMS_EQUAL,
            match_result_obj.higher_team
        )

        self.assertFalse(match_result_obj.is_higher_team_win())
        self.assertFalse(match_result_obj.is_underdog_win())
        self.assertTrue(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.TEAM_A_WIN,
            match_result_obj.result
        )

        match_result_obj = rugby_rankings.match_result.MatchResult(3, 0, 3, 0)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.HIGHER_A,
            match_result_obj.higher_team
        )

        self.assertTrue(match_result_obj.is_higher_team_win())
        self.assertFalse(match_result_obj.is_underdog_win())
        self.assertFalse(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.TEAM_A_WIN,
            match_result_obj.result
        )

    def test_match_result_team_b_win(self):
        match_result_obj = rugby_rankings.match_result.MatchResult(3, 0, 0, 3)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.HIGHER_A,
            match_result_obj.higher_team
        )

        self.assertFalse(match_result_obj.is_higher_team_win())
        self.assertTrue(match_result_obj.is_underdog_win())
        self.assertFalse(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.TEAM_B_WIN,
            match_result_obj.result
        )

        match_result_obj = rugby_rankings.match_result.MatchResult(0, 3, 0, 3)

        self.assertEqual(
            rugby_rankings.match_result.MatchResult.HIGHER_B,
            match_result_obj.higher_team
        )

        self.assertTrue(match_result_obj.is_higher_team_win())
        self.assertFalse(match_result_obj.is_underdog_win())
        self.assertFalse(match_result_obj.is_equals_win())

        self.assertEqual(
            match_result_obj.TEAM_B_WIN,
            match_result_obj.result
        )