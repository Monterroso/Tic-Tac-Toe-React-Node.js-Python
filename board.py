import copy

class grid:
  """Class representing a grid

  Members: 
    grid {list of (list of (int))} -- The 2d array of the grid 
    x_dist {integer} -- The size of the grid in the X dimension
    y_dist {integer} -- The size of the grid in the Y dimension

  Methods:
    __init__(integer, integer, list of (list of (int))) -- Creates the empty grid, or copies a grid if an array is given
    get_at(tuple of (integer, integer)) -- Gets the value at the specified x,y location in the grid
    place_at(integer, tuple of (integer, integer)) -- Places the id at the tuple location
    copy() -- Copies the grid object and returns the new object

  """
  def __init__(self, x_dist, y_dist, grid=None):
    """Creates an empty Board with given dimensions if grid is None, copies grid otherwise

    Arguments: 
      x_dist {integer} -- The size of the grid in the X dimension
      y_dist {integer} -- The size of the grid in the Y dimension

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
      player_id {integer} -- The player id to be placed on the grid at the location
      location {tuple of (integer, integer)} -- The tuple to represent the x,y location of the slot

    """
    x_pos = location[0]
    y_pos = location[1]

    #check if the location is currently occupied
    if self.grid[x_pos][y_pos] is not 0:
      raise Exception("The location ({0}, {1}) is occupied with {3}, you cannot place an id there".format(
        x_pos, y_pox, self.grid[x_pos][y_pos]))

    #sets the id
    self.grid[x_pos][y_pos] = player_id

  def copy(self):
    """Returns a copy of this grid

    Returns: 
      {grid} -- A deep copy of this grid

    """

    return grid(self.x_dist, self.y_dist, self.grid)