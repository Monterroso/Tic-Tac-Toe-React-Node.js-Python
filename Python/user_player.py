from player import Player 
import random

class UserPlayer(Player):
  """Class representing a user

  A UserPlayer is given a function that, when called, will choose a state

  """

  def __init__(self, user_function, player_id):
      super(UserPlayer, self).__init__(player_id)

      self.user_function = user_function

  def choose_state(self, player_choices):
    """Overriding the method in Player, picks a random state

    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """

    return self.user_function(player_choices)

