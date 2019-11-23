import copy
import json
import unittest

class Board:
  """Class representing a board

  Members: 
    grid {list of (list of (int))} -- The 2d array of the grid 
    x_dist {integer} -- The size of the grid in the X dimension
    y_dist {integer} -- The size of the grid in the Y dimension

  Methods:
    __init__(integer, integer, list of (list of (int))) -- Creates the empty grid, or copies a grid if an array is given
    __eq__(object) -- Overloads the equality operator, two boards are equal if their grids are equal
    get_at(tuple of (integer, integer)) -- Gets the value at the specified x,y location in the grid
    place_at(integer, tuple of (integer, integer)) -- Places the id at the tuple location
    get_states(integer) -- Gets all possible states for a given player
    check_win(integer) -- Checks if the player is in a win state (only horizontal and vertical)
    check_tie() -- Checks if current state is in a tie state (only if the board is completely filled)
    copy() -- Copies the grid object and returns the new object
    to_JSON() -- Returns this board in JSON format
    

  """

  def __init__(self, x=None, y=None, grid=None):
    """Creates an empty Board with given dimensions if grid is None, copies grid otherwise

    Arguments: 
      x_dist {integer} -- The size of the grid in the X dimension
      y_dist {integer} -- The size of the grid in the Y dimension

    Raises:
      AttributeError -- Exception if the given grid is not uniform in it's height
      AttributeError -- Exception if the grid contains a non-integer value
    """

    if grid is None: 
      self.x_dist = x
      self.y_dist = y
      self.grid = [[0 for _ in range(y)] for _ in range(x)]
    else: 
      #Check to be sure the dimensions are valid
      temp_x = len(grid)
      temp_y = len(grid[0])
      for x in range(len(grid)):
        if len(grid[x]) != temp_y:
          raise  AttributeError("The given grid does not have columns of the same length")
        for y in range(len(grid[x])):
          if not isinstance(grid[x][y], int):
            raise  AttributeError("The given grid contains a non integer value at {0}".format((x, y)))

      self.x_dist = temp_x
      self.y_dist = temp_y
      self.grid = copy.deepcopy(grid)

  def __eq__(self, obj):
    """Overrides the == operator, two board objects are equal if their grids are the same

    Arguments:
      obj {object} -- The object we are comparing to self

    """

    return isinstance(obj, Board) and obj.grid == self.grid



  def get_at(self, location):
    """Returns the value at the specified location

    Arguments:
      location {tuple of (integer, integer)} -- The tuple to represent the x,y location of the slot

    Returns:
      {integer} -- The value of the specified slot, 0 if empty, or a player_id if not empty

    Raises: 
      IndexError -- Raised when a location outside of the grid space is attempted to be accessed. 

    """
    x_look = location[0]
    y_look = location[1]
    if x_look >= self.x_dist or y_look >= self.y_dist:
      raise IndexError("{0} is out of the range of this grid, of width {1} and height {2}".format((x_look,y_look),\
        self.x_dist, self.y_dist))

    return self.grid[location[0]][location[1]]

  def place_at(self, player_id, location): 
    """Places the player_id at the location given by the location

    Arguments:
      player_id {integer} -- The player id to be placed on the grid at the location
      location {tuple of (integer, integer)} -- The tuple to represent the x,y location of the slot

    Raises: 
      AttributeError -- Error if the location to place is already occupied. 
      IndexError -- Error if the location is out of bounds
    """
    x_pos = location[0]
    y_pos = location[1]

    #check if the location is currently occupied
    if x_pos >= self.x_dist or y_pos >= self.y_dist:
      raise IndexError("The location {0} is out of bounds")
    if self.grid[x_pos][y_pos] is not 0:
      raise  AttributeError("The location {0} is occupied with {1}, you cannot place an id there".format(\
        (x_pos, y_pos), self.grid[x_pos][y_pos]))

    #sets the id
    self.grid[x_pos][y_pos] = player_id

  
  def get_states(self, player_id):
    """Returns all possible game states the player can make

    Arguments:
      player_id {integer} -- The id of the player
  
    Returns:
      {list of (Board)} -- The list of Boards that the player can branch to
    """

    boards = []

    #Double for loop through x and y coordinates
    for x in range(self.x_dist):
      for y in range(self.y_dist):
        #check if space is free
          #if free, dupblicate board, add id to location
          #add board to boards
        if self.get_at((x, y)) == 0:
          new_board = self.copy()
          new_board.place_at(player_id, (x, y))
          boards.append(new_board)

    #return boards
    return boards

  def check_win(self, win_amount, player_id):
    """Checks if the player has won

    Arguments:
        win_amount {integer} -- The number of consecutive tiles to win
        player_id {integer} -- The id of the player we are checking


      Returns: 
        {boolean} -- Returns true if the player has won, false if they have not

    """

    #Row Check
    for x in range(self.x_dist):
      counter = 0
      for y in range(self.y_dist):
        if self.get_at((x,y)) == player_id:
          counter += 1
        else: 
          counter = 0

        if counter == win_amount: 
          return True

    #Column Check
    for y in range(self.y_dist):
      counter = 0
      for x in range(self.x_dist):
        if self.get_at((x,y)) == player_id:
          counter += 1
        else: 
          counter = 0

        if counter == win_amount: 
          return True

    #If hasn't returned true, then it's false
    return False

  def check_tie(self):
    """Checks if there is no way a player can win, currently returns true if and only if the board is filled

    Returns:
      {boolean} -- Returns true if the player is not able to win, false if they still can. 

    """
    for x in range(self.x_dist):
      for y in range(self.y_dist):
        if self.get_at((x,y)) == 0:
          return False

    return True

  def copy(self):
    """Returns a copy of this grid

    Returns: 
      {Board} -- A deep copy of this grid

    """

    return Board(grid=self.grid)

  def to_json(self):
    """Returns this board as a JSON object

    Returns:
      {JSON} -- This object encoded as a JSON, info on the grid, the x and y coordinates

    """

    object_json = dict()

    object_json["Type"] = self.__class__.__name__
    board_obj = dict()
    board_obj["x"] = self.x_dist
    board_obj["y"] = self.y_dist
    board_obj["grid"] = self.grid
    object_json["Object"] = board_obj

    return object_json

class BoardTests(unittest.TestCase):
  """Full suit of testing for the board and it's functionality

  """

  def test_init(self):
    """Suite testing the init functionality

    """
    a_x_dist = 3
    a_y_dist = 5
    a_board = Board(a_x_dist, a_y_dist)
    a_grid_copy = [[0 for _ in range(a_y_dist)] for _ in range(a_x_dist)]

    #Check to be sure a_Board has proper attributes
    self.assertEqual(a_board.x_dist, a_x_dist, "The x distance was not properly set")
    self.assertEqual(a_board.y_dist, a_y_dist, "The y distance was not properly set")
    self.assertEqual(len(a_board.grid), a_x_dist, "The width of the grid was not properly set")
    self.assertEqual(len(a_board.grid[2]), a_y_dist, "The height of the grid was not properly set")

    self.assertEqual(a_board.grid, a_grid_copy, "One of the values in the grid was not set")

    b_x_dist = 20
    b_y_dist = 2
    b_board = Board(b_x_dist, b_y_dist)
    b_grid_copy = [[0 for _ in range(b_y_dist)] for _ in range(b_x_dist)]

    #Check to be sure a_Board has proper attributes
    self.assertEqual(b_board.x_dist, b_x_dist, "The x distance was not properly set")
    self.assertEqual(b_board.y_dist, b_y_dist, "The y distance was not properly set")
    self.assertEqual(len(b_board.grid), b_x_dist, "The width of the grid was not properly set")
    self.assertEqual(len(b_board.grid[2]), b_y_dist, "The height of the grid was not properly set")

    self.assertEqual(b_board.grid, b_grid_copy, "One of the values in the grid was not set")

    #Check to make sure that the board is properly cloned
    c_x_dist = 5
    c_y_dist = 3
    c_grid = [[0,0,0],[1,2,1],[0,1,1],[2,2,2],[1,0,0]]
    c_grid_copy =  [[0,0,0],[1,2,1],[0,1,1],[2,2,2],[1,0,0]]

    c_board = Board(grid=c_grid)

    self.assertEqual(c_board.x_dist, c_x_dist, "The x distance was not properly set")
    self.assertEqual(c_board.y_dist, c_y_dist, "The y distance was not properly set")
    self.assertEqual(len(c_board.grid), c_x_dist, "The width of the grid was not properly set")
    self.assertEqual(len(c_board.grid[2]), c_y_dist, "The height of the grid was not properly set")

    self.assertEqual(False, c_board.grid is c_grid, "The grid was not deep copied")

    self.assertEqual(c_board.grid, c_grid_copy, "One of the values in the grid was not properly copied over")
    
  def test_init_exceptions(self):
    """Suite testing the behavior of the exceptions in the init method

    """

    #Check proper exceptions are raised
    uneven_board = [[1,2,3],[0,0],[1,2,5]]
    self.assertRaises(AttributeError, Board, grid=uneven_board)

    non_int_board = [[1,2],[1,3],['a',7]]
    self.assertRaises(AttributeError, Board, grid=non_int_board)

  def test_get_at(self):
    """Suite testing the get_at(self, location) method

    """

    a_grid = [[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35]]
    a_board = Board(grid=a_grid)

    self.assertEqual(a_board.get_at((0,4)), 5)
    self.assertEqual(a_board.get_at((3,3)), 34)
    self.assertEqual(a_board.get_at((2,1)), 22)
    self.assertEqual(a_board.get_at((0,4)), 5)

  def test_get_at_exceptions(self):
    """Suite testing the behavior of the exceptions of the get_at method

    """
    a_grid = [[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33],[40,41,42,43]]
    a_board = Board(grid=a_grid)

    self.assertRaises(IndexError, a_board.get_at, (5,5))

  def test_place_at(self):
    """Suite testing the place_at method

    """

    a_grid = [[0,0],[1,2],[1,0],[2,0],[5,5],[0,0]]
    a_complete_grid = [[3,1],[1,2],[1,2],[2,0],[5,5],[0,5]]
    a_board = Board(grid=a_grid)

    a_board.place_at(1, (0,1))
    a_board.place_at(2, (2,1))
    a_board.place_at(5, (5,1))
    a_board.place_at(3, (0,0))

    for x in range(a_board.x_dist):
      for y in range(a_board.y_dist):
        self.assertEqual(a_board.grid[x][y], a_complete_grid[x][y],\
          "The value at {0} was not properly placed".format((x,y)))
    

  def test_place_at_exceptions(self):
    """Suite testing the exceptions raised in the place_at method

    """

    a_grid = [[0,2,3,4,5,6,0]]
    a_board = Board(grid=a_grid)

    self.assertRaises(AttributeError, a_board.place_at, 1,(0,4))
    self.assertRaises(IndexError, a_board.place_at, 2,(2,2))

  def test_get_states(self):
    """Suite testing that all possible states are computed by the game given a player

    """

    a_x_dist = 5
    a_y_dist = 4
    a_board = Board(a_x_dist, a_y_dist)

    a_player = 1

    a_board_states = a_board.get_states(a_player)

    for x in range(a_x_dist):
      for y in range(a_y_dist):
        temp_board = a_board.copy()
        temp_board.place_at(a_player, (x, y))
        # self.assertTrue(temp_board.grid in [state.grid for state in a_board_states])
        self.assertTrue(temp_board in state for state in a_board_states)

    self.assertEqual(len(a_board_states), a_x_dist * a_y_dist)


    b_x_dist = 4
    b_y_dist = 3
    b_grid = [[1,0,0],[2,0,2],[5,0,3],[1,1,1]]

    b_player = 2

    b_state_results = [Board(grid=[[1,b_player,0],[2,0,2],[5,0,3],[1,1,1]]),
    Board(grid=[[1,0,b_player],[2,0,2],[5,0,3],[1,1,1]]),
    Board(grid=[[1,0,0],[2,b_player,2],[5,0,3],[1,1,1]]),
    Board(grid=[[1,0,0],[2,0,2],[5,b_player,3],[1,1,1]])]

    b_board = Board(grid=b_grid)

    b_board_states = b_board.get_states(b_player)

    # self.assertTrue(all(b_brd in [state.grid for state in b_board_states] for b_brd in b_state_results))
    for b_brd in b_state_results:
      self.assertTrue(b_brd in b_board_states, "{0} is not in {1}".format(b_brd,b_board_states))
    # self.assertTrue(all(b_brd in b_board_states for b_brd in b_state_results))

    self.assertEqual(len(b_state_results), len(b_board_states))

  def test_check_win(self):
    """Suite testing that wins are properly caught

    """

    #Checks a few cases of not having a win, along with a few of having a win. 
    
    #Not wins for player 1
    not_player = 1

    not_a_grid = [[1,0,0],[1,1,0],[0,0,1],[0,1,1]]
    not_b_grid = [[1,2,2,1,1],[0,2,1,1,1],[2,2,2,1,1]]
    not_c_grid = [[0,0],[0,0],[0,0],[0,0]]

    not_a_board = Board(grid=not_a_grid)
    not_b_board = Board(grid=not_b_grid)
    not_c_board = Board(grid=not_c_grid)

    not_a_win = 3
    not_b_win = 4
    not_c_win = 1

    self.assertFalse(not_a_board.check_win(not_a_win, not_player))
    self.assertFalse(not_b_board.check_win(not_b_win, not_player))
    self.assertFalse(not_c_board.check_win(not_c_win, not_player))

    #Wins for player 2
    
    yes_player = 2

    yes_a_grid = [[2,2,2],[1,0,0],[0,0,0],[2,0,0],[1,1,1]]
    yes_b_grid = [[0,0,0],[1,1,1],[1,1,1]]
    yes_c_grid = [[0,1,2,2,0],[2,0,1,2,1],[0,0,0,2,0],[1,1,1,2,1],[0,0,0,2,1],[0,1,2,2,1]]

    yes_a_board = Board(grid=yes_a_grid)
    yes_b_board = Board(grid=yes_b_grid)
    yes_c_board = Board(grid=yes_c_grid)

    yes_a_win = 3
    yes_b_win = 0
    yes_c_win = 6

    self.assertTrue(yes_a_board.check_win(yes_a_win, yes_player))
    self.assertTrue(yes_b_board.check_win( yes_b_win, yes_player))
    self.assertTrue(yes_c_board.check_win(yes_c_win, yes_player))



  def test_check_tie(self):
    """Suite testing that ties are properly caught

    """

    #Just check if not all are open, vs all being open
    not_tie_a_grid = [[0,0,0],[1,0,0],[0,0,0],[0,0,0],[0,0,0]]
    
    not_tie_a_board = Board(grid=not_tie_a_grid)

    self.assertFalse(not_tie_a_board.check_tie())

    tie_a_grid = [[1 for _ in range(5)] for _ in range(10)]

    tie_a_board = Board(grid=tie_a_grid)

    self.assertTrue(tie_a_board.check_tie())


  def test_copy(self):
    """Suite testing the functionality of the copy method

    """

    a_grid = [[0,2,3,4,5,6,0]]
    a_board = Board(grid=a_grid)
    b_board = a_board.copy()

    self.assertEqual(False, a_board is b_board, "The boards are the same and a deepy copy wasn't created")

  def test_to_JSON(self):
    """Suite testing that a JSON object is properly created from this board 

    """
    a_x_dist = 5
    a_y_dist = 4
    a_grid = [[1,2,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0],[2,2,2,2]]
    a_grid_string = "[[1, 2, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [2, 2, 2, 2]]"
    a_board = Board(grid=a_grid)
    a_board_string = '{{"Type": "Board", "Object": {{"x": {0}, "y": {1}, "grid": {2}}}}}'\
      .format(a_x_dist, a_y_dist, a_grid_string)

    a_board_json = a_board.to_json()

    print(a_board_json)

    self.assertEqual(a_board_json, a_board_string)



if __name__ == '__main__':
    unittest.main()