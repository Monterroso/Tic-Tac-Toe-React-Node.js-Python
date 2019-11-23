from player import Player 
import random

class UserPlayer(Player):
  """Class representing a user

  A UserPlayer has it's choice set whenever it seeks to make a move

  """

  def __init__(self, player_id):
      super(UserPlayer, self).__init__(player_id)

      #The choice we use for 
      self.choice = -1

  def choose_state(self, player_choices):
    """Overriding the method in Player, picks a random state
    
    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """

    if self.choice == -1:
      raise AttributeError("The choice must be set for the player before it can choose a state")

    player_choice = self.choice
    self.choice = -1
    return player_choice


  def pause_execution(self):
    """Overriding the method in Player, a user player should pause execution

    Returns:
      {boolean} -- Whether this player should suspend execution of the game

    """

    return True

  def set_choice(self, player_choice):
    """Method used to set this player's next choice

    Arguments:
      player_choice {integer} -- The choice to be used for this player when choose_state is called

    """

    self.choice = player_choice



