from player import Player 
import random

class RandomPlayer(Player):
  """Class representing a random player

  A RandomPlayer returns a random state when given states

  """

  def choose_state(self, player_choices):
    """Overriding the method in Player, picks a random state

    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """

    return random.randint(0, len(player_choices) - 1)

