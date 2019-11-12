import random

class Player:
  """The class to hold information pertaining to a player, to be extended

  Members: 
    player_id {integer} -- The unique id of the player in question, cannot be 0

  Methods: 
    __init__ (integer) -- Creates a player with the unique integer id
    choose_state (list of (Board)) -- Given the board states, chooses one and returns an integer

  """
 
  def __init(self, player_id):
    """Sets the player's id, and adds it to the list of players

    Arguments:
      player_id {integer} -- The player's id, cannot be 0

    """
    self.player_id = player_id
    players[player_id] = self

  def choose_state(player_choices):
    """Given a set of choices, returns a value of one of the options. 

    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """
    return random.randint(0, len(player_choices))


