# Rugby Rankings

Python library for calculating rugby ranking points.

This library is a Python version of [php rugby rankings](https://github.com/RhodriM/rugbyRankings). The php library was itself an exercise in OO, tools etc; therefore some code may be slightly over-OOP-engineered - especially for Python. As a newcomer to Python I have tried to do things 'the Python way', even where it goes against my OOP/Java-ish instincts, but if there are any obvious cases in this repo of where something could be done better in Python please let me know.

## Usage

Requires Python 3.

### rugby_rankings package

The main intended usage is for rugby_rankings/ as a package for other projects. The main entry point for the package is main.Main

```python
from rugby_rankings import ratings_input,main,ratings_output

r_input = ratings_input.RatingsInput(
    team_a_rating,
    team_b_rating,
    score_a,
    score_b,
    neutral_venue,
    world_cup
)
r_main = main.Main(r_input)

r_output = r_main.calculate()

new_rating_a = r_output.get_team_a_rating()
new_rating_b = r_output.get_team_b_rating()
```

### Command line interface

A command line interface is also provided by rugby_rankings.py:
```bash
$ python3 rugby_rankings.py --help
usage: rugby_rankings.py [-h] [--neutral] [--world_cup] [--simple] [--verbose]
                         rating_a rating_b score_a score_b

positional arguments:
  rating_a     the ranking points of team a
  rating_b     the ranking points of team b
  score_a      the score of team a
  score_b      the score of team b

optional arguments:
  -h, --help   show this help message and exit
  --neutral    game is played at neutral venue
  --world_cup  game is world cup game
  --simple     less verbose output
  --verbose    more verbose output
```

For example: if Wales were to beat England 30-3 at Twickenham ;-)
```bash
$ python3 rugby_rankings.py 90.14 81.73 3 33 --verbose
Team A score:              03
Team B score:              33
World Cup game:            False
Neutral Venue:             False
Team A rating before game: 90.14
Team B rating before game: 81.73
Team A rating after game:  87.14
Team B rating after game:  84.73
Team A change:             -3.00
Team B change:             +3.00
```

Adding a --simple flag will produce less verbose output, more suitable for piping to something else:
```bash
$ python3 rugby_rankings.py 90.14 81.73 3 33 --simple
87.14,84.73
```

## Contributing

See [Contributing Guide](CONTRIBUTING.md)

## Credits

- [Rhodri Morris](https://github.com/RhodriM)
- [All Contributors](https://github.com/RhodriM/rugbyRankings/contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
