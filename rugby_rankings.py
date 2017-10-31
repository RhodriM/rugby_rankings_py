"""
A command line interface for the rugby_rankings package
"""

import argparse
from rugby_rankings import *


parser = argparse.ArgumentParser()
parser.add_argument("rating_a", help="the ranking points of team a", type=float)
parser.add_argument("rating_b", help="the ranking points of team b", type=float)
parser.add_argument("score_a", help="the score of team a", type=int)
parser.add_argument("score_b", help="the score of team b", type=int)
parser.add_argument("--neutral", help="game is played at neutral venue", action="store_true")
parser.add_argument("--world_cup", help="game is world cup game", action="store_true")
parser.add_argument("--simple", help="less verbose output", action="store_true")
parser.add_argument("--verbose", help="more verbose output", action="store_true")
args = parser.parse_args()

r_input = ratings_input.RatingsInput(
    args.rating_a,
    args.rating_b,
    args.score_a,
    args.score_b,
    args.neutral,
    args.world_cup
)
r_main = main.Main(r_input)

r_output = r_main.calculate()

if args.verbose:
    print('Team A score:              ' + '{:02d}'.format(args.score_a))
    print('Team B score:              ' + '{:02d}'.format(args.score_b))
    print('World Cup game:            ' + str(args.world_cup))
    print('Neutral Venue:             ' + str(args.neutral))
    print('Team A rating before game: ' + '{0:.2f}'.format(args.rating_a))
    print('Team B rating before game: ' + '{0:.2f}'.format(args.rating_b))

if args.simple and not args.verbose:
    print('{0:.2f}'.format(r_output.get_team_a_rating())
          + ',' + '{0:.2f}'.format(r_output.get_team_b_rating())
         )
else:
    print('Team A rating after game:  '
          + '\033[1;30m{0:.2f}'.format(r_output.get_team_a_rating()) + '\033[1;m')
    print('Team B rating after game:  '
          + '\033[1;30m{0:.2f}'.format(r_output.get_team_b_rating()) + '\033[1;m')

if args.verbose and not args.simple:
    team_a_change = r_output.get_team_a_rating() - args.rating_a
    team_b_change = r_output.get_team_b_rating() - args.rating_b
    if team_a_change > 0:
        color = '32'
    elif team_a_change < 0:
        color = '31'
    else:
        color = '30'
    print('Team A change:             '
          + '\033[1;' + color + 'm{0:+.2f}\033[1;m'.format(team_a_change)
         )

    if team_b_change > 0:
        color = '32'
    elif team_b_change < 0:
        color = '31'
    else:
        color = '30'
    print('Team B change:             '
          + '\033[1;' + color + 'm{0:+.2f}\033[1;m'.format(team_b_change)
         )
