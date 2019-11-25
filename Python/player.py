import json
import unittest

class Player:
  """The class to hold information pertaining to a player, to be extended

  Members: 
    player_id {integer} -- The unique id of the player in question, cannot be 0

  Methods: 
    __init__ (integer) -- Creates a player with the unique integer id
    get_id() -- returns the id of the player
    choose_state (list of (Board)) -- Given the board states, chooses one and returns an integer
    pause_execution () -- Returns true if the player should stop execution
    to_JSON() -- Converts the player into a JSON object

  """
 
  def __init__(self, player_id):
    """Sets the player's id, and adds it to the list of players

    Arguments:
      player_id {integer} -- The player's id, cannot be 0

    Raises:
      AttributeError -- If you attempt to assign a player_id of 0

    """
    
    if player_id <= 0:
      raise AttributeError("You cannot assign 0 or lower to the player_id")

    self.player_id = player_id

  def __eq__(self, obj):
    """Two players are equal if they have the same id and are of the same class

    Arguments:
      obj {object} -- The object we are comparing to self

    """
    return type(obj) == type(self) and self.player_id == obj.player_id

  def get_id(self):
    """Returns the id of the player

    Returns:
      {integer} -- The id of the player

    """

    return self.player_id

  def choose_state(self, player_choices):
    """Given a set of choices, returns a value of one of the options. 

    Arguments: 
      player_choices {list of (Board)} -- A list of possible board states to branch to

    Returns:
      {integer} -- location of the board state to be selected

    """
    raise NotImplementedError("The behavior of choose_state must be overriden")

  def pause_execution(self):
    """Returns true or false if execution should be stopped, in the case of waiting for a player

    Returns: 
      {Boolean} -- True or false if execution should be suspended

    """

    return False

  def to_json(self):
    """Returns this Player as a JSON object

    Returns:
      {JSON} -- This object encoded as a JSON, should be overriden

    """

    object_json = dict()

    object_json["Type"] = self.__class__.__name__
    object_json["Object"] = {"player_id": self.player_id}

    return json.dumps(object_json) 


class PlayerTests(unittest.TestCase):
  """The suite to test the player class

  """

  def test_init(self):
    """Suite testing that the player is set up

    """

    a_player = Player(1)
    self.assertEqual(a_player.player_id, 1)

  def test_init_exceptions(self):
    """Suite testing that the proper exceptions are thrown for the player

    """

    self.assertRaises(AttributeError, Player, 0)

  def test_choose_state(self):
    """Suite testing that a state is properly chosen

    """

    a_player = Player(1)

    states = [5,[], "b", None, True, "Bananas"]

    self.assertRaises(NotImplementedError, a_player.choose_state, states)

  def test_to_json(self):
    """Suite testing that a player is properly stored as a JSON
    
    """

    #All the needs to be tested is that the JSON is formatted properly 

    a_player_id = 1
    a_player = Player(a_player_id)
    a_player_json = a_player.to_json()

    self.assertEqual(a_player_json, '{{"Type": "Player", "Object": {{"player_id": {0}}}}}'.format(a_player_id))


if __name__ == '__main__':
    unittest.main()
    