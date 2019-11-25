from player import Player

class ZeroPlayer(Player):
  """A zero player always chooses the first option given to them
  
  """

  def choose_state(self, player_choices):
    """This class always returns 0. 

    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """

    return 0