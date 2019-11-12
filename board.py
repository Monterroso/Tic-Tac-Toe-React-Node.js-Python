import copy

class Board:
  """Class representing a board

  Members: 
    board {list of (list of (int))} -- The 2d array of the board 
    x_dist {integer} -- The size of the board in the X dimension
    y_dist {integer} -- The size of the board in the Y dimension

  Methods:
    __init__(integer, integer, list of (list of (int))) -- Creates the empty board, or copies a board if an array is given
    place_at(integer, tuple of (integer, integer)) -- Places the id at the tuple location
    copy() -- Copies the board object and returns the new object

  """
  def __init__(self, x_dist, y_dist, grid=None):
    """Creates an empty board with given dimensions

    Arguments: 
      x_dist {integer} -- The size of the board in the X dimension
      y_dist {integer} -- The size of the board in the Y dimension

    """
    self.x_dist = x_dist
    self.y_dist = y_dist

    if grid is None: 
      self.grid = [[0 for _ in range(y_dist)] for _ in range(x_dist)]
    else: 
      self.grid = copy.deepcopy(grid)

  def get_at(self, location):
    """Returns the value at the specified location

    Arguments:
      location {tuple of (integer, integer)} -- The tuple to represent the x,y location of the slot

    Returns:
      {integer} -- The value of the specified slot, 0 if empty, or a player_id if not empty

    """
    return self.grid[location[0]][location[1]]

  def place_at(self, player_id, location): 
    """Places the player_id at the location given by the location

    Arguments:
      player_id {integer} -- The player id to be placed on the board at the location
      location {tuple of (integer, integer)} -- The tuple to represent the x,y location of the slot

    """
    x_pos = location[0]
    y_pos = location[1]

    #check if the location is currently occupied
    if self.board[x_pos][y_pos] is not 0:
      raise Exception("The location ({0}, {1}) is occupied with {3}, you cannot place an id there".format(
        x_pos, y_pox, self.grid[x_pos][y_pos]))

    #sets the id
    self.grid[x_pos][y_pos] = player_id

  def copy(self):
    """Returns a copy of this board

    Returns: 
      {Board} -- A deep copy of this board

    """

    return Board(self.x_dist, self.y_dist, self.grid)