"""
Defines InvalidMatchResultException
"""

class InvalidMatchResultException(Exception):
    """
    An exception for invalid match results - must be team a win, team b win or draw
    """
    def __init__(self, value):
        super().__init__()
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)
