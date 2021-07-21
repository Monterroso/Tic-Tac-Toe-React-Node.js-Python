from board import Board
from player import Player

import unittest

"""A module containing functions that do things to the board. 

#     get_states(board, integer) -- Gets all possible states for a given player
#     check_win(board, integer) -- Checks if the player is in a win state (only horizontal and vertical)
#     check_tie(board) -- Checks if current state is in a tie state (only if the board is completely filled)

"""

def get_states(brd, player_id):
    """Returns all possible game states the player can make

    Arguments:
      brd {Board} -- The board we are using to generate states
      player_id {integer} -- The id of the player
  
    Returns:
      {list of (Board)} -- The list of Boards that the player can branch to
    """

    boards = []

    #Double for loop through x and y coordinates
    for x in range(brd.x_dist):
      for y in range(brd.y_dist):
        #check if space is free
          #if free, dupblicate board, add id to location
          #add board to boards
        if brd.get_at((x, y)) == 0:
          new_board = brd.copy()
          new_board.place_at(player_id, (x, y))
          boards.append(new_board)

    #return boards
    return boards


def check_win(brd, win_amount, player_id):
  """Checks if the player has won

  Arguments:
      brd {Board} -- The board to check
      win_amount {integer} -- The number of consecutive tiles to win
      player_id {integer} -- The id of the player we are checking


    Returns: 
      {boolean} -- Returns true if the player has won, false if they have not

  """

  #Row Check
  for x in range(brd.x_dist):
    counter = 0
    for y in range(brd.y_dist):
      if brd.get_at((x,y)) == player_id:
        counter += 1
      else: 
        counter = 0

      if counter == win_amount: 
        return True

  #Column Check
  for y in range(brd.y_dist):
    counter = 0
    for x in range(brd.x_dist):
      if brd.get_at((x,y)) == player_id:
        counter += 1
      else: 
        counter = 0

      if counter == win_amount: 
        return True

  #If hasn't returned true, then it's false
  return False


def check_tie(brd):
    """Checks if there is no way a player can win, currently returns true if and only if the board is filled

    Returns:
      {boolean} -- Returns true if the player is not able to win, false if they still can. 

    """
    for x in range(brd.x_dist):
      for y in range(brd.y_dist):
        if brd.get_at((x,y)) == 0:
          return False

    return True

class BoardFunctionTest(unittest.TestCase):
  """Suite that tests functions that act on the board

  """
  def test_get_states(self):
    """Suite testing that all possible states are computed by the game given a player

    """

    a_x_dist = 5
    a_y_dist = 4
    a_board = Board(a_x_dist, a_y_dist)

    a_player = 1

    a_board_states = get_states(a_board, a_player)

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

    b_board_states = get_states(b_board, b_player)

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

    self.assertFalse(check_win(not_a_board, not_a_win, not_player))
    self.assertFalse(check_win(not_b_board, not_b_win, not_player))
    self.assertFalse(check_win(not_c_board, not_c_win, not_player))

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

    self.assertTrue(check_win(yes_a_board, yes_a_win, yes_player))
    self.assertTrue(check_win(yes_b_board, yes_b_win, yes_player))
    self.assertTrue(check_win(yes_c_board, yes_c_win, yes_player))



  def test_check_tie(self):
    """Suite testing that ties are properly caught

    """

    #Just check if not all are open, vs all being open
    not_tie_a_grid = [[0,0,0],[1,0,0],[0,0,0],[0,0,0],[0,0,0]]
    
    not_tie_a_board = Board(grid=not_tie_a_grid)

    self.assertFalse(check_tie(not_tie_a_board))

    tie_a_grid = [[1 for _ in range(5)] for _ in range(10)]

    tie_a_board = Board(grid=tie_a_grid)

    self.assertTrue(check_tie(tie_a_board))

if __name__ == '__main__':
  unittest.main()