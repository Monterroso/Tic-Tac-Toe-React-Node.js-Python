from board import Board
import board_functions as bf
from player import Player
from random_player import RandomPlayer
import unittest


class Game:
  """Class that holds all information about a tic-tac-toe game

  Members: 
    players {list of (Player)} -- The list of Player objects in order to play the game
    x_dist {integer} -- The number of tiles in the X direction for the Board
    y_dist {integer} -- The number of tiles in the Y direction for the Board
    turn_number {integer} -- The turn number of the game, starts at 0
    board {Board} -- The current Board in the game
    board_history {list of (Board)} -- The list of Board objects representing the game's history
    num_to_win {integer} -- The number of tiles horizontally or vertically a player needs to win

  Methods: 
    __init__(list of (Player), integer, integer) -- Sets up basing game information
    play_game() -- Plays the game to completion
    _increment_turn() -- Increments the turn counter
    _end_game() -- Does additional work when the game reaches an end state
    get_current_player() -- Gets the id of the current player
    get_player({integer}) -- Gets the player object given the id of the player

  """

  def __init__(self, players, x_dist, y_dist, num_to_win):
    """Creates a game that can be started from start to finish

    Creates the game board and sets turn counter to 0

    Arguments: 
      players {list of (Player)} -- The players given in order to play the tic-tac-toe game
      x_dist {integer} -- The number of tiles in the X direction
      y_dist {integer} -- The number of tiles in the Y direction
      num_to_win {integer} -- The number of tiles in a row or horizontally one needs to win

    """
    self.players = players
    self.x_dist = x_dist
    self.y_dist = y_dist

    self.turn_number = 0
    self.board = Board(x_dist, y_dist)
    self.board_history = []
    self.num_to_win = num_to_win

    self.max_turns = 1000

    self.winner = None

  #####################         ##################### 
  #                    Play Game                    #
  #####################         ##################### 

  def play_game(self):
    """Plays the tic-tac-toe game to completion

    """ 
    cur_player = self.get_current_player()

    #Loop game until completion
    while self.turn_number <= self.max_turns:
      #Store board at current counter
      self.board_history.append(self.board)

      #Check for win or tie
        #If either, call end game with respective parameters
      if bf.check_win(self.board, self.num_to_win, cur_player):
        self._end_game(cur_player)
        return
      if bf.check_tie(self.board):
        self._end_game()
        return

      #Incriment turn counter
      self._increment_turn()

      #Get current player
      cur_player = self.get_current_player()

      player_object = self.get_player(cur_player)

      #Get all the states
      next_states = bf.get_states(self.board, cur_player)

      #Get board states for current player
      chosen_board = next_states[player_object.choose_state(next_states)]

      #Update board state
      self.board = chosen_board

    

  def _increment_turn(self):
    """Increments the turn counter 
    
    """

    self.turn_number += 1

  def _end_game(self, winner_id=None): 
    """Called when the game has reached a terminal state

    Arguments:
      winner_id {integer} -- The id of the winning player, None if game is a tie

    """
    if winner_id == None:
      print("The game was a tie!")
    else:
      print("{0} has won the game!".format(winner_id))
    self.winner = winner_id

  #####################         ##################### 
  #                    Utilities                    #
  #####################         ##################### 

  def get_current_player(self):
    """Returns the id of the current player 

    Returns:
      {integer} -- The id of the current player
    
    """

    return self.players[(self.turn_number - 1) % len(self.players)].get_id()

  def get_player(self, player_id):
    """Returns the player given the player's id

    Arguments: 
      player_id {integer} -- The id of the Player object we want

    Returns: 
      {Player} -- The Player object we seek to return

    """

    for player in self.players:
      if player.player_id == player_id:
        return player

    raise Exception("A player with the given id {0} was not found in the player list".format(player_id))

  def get_history(self):
    """Returns the history of the board currently

    Returns:
      {list of (Board)} -- The history of the board

    """

    return self.board_history

# Members: 
#     players {list of (Player)} -- The list of Player objects in order to play the game
#     x_dist {integer} -- The number of tiles in the X direction for the Board
#     y_dist {integer} -- The number of tiles in the Y direction for the Board
#     turn_number {integer} -- The turn number of the game, starts at 0
#     board {Board} -- The current Board in the game
#     board_history {list of (Board)} -- The list of Board objects representing the game's history
#     num_to_win {integer} -- The number of tiles horizontally or vertically a player needs to win

#   Methods: 
#     __init__(list of (Player), integer, integer) -- Sets up basing game information
#     play_game() -- Plays the game to completion
#     _increment_turn() -- Increments the turn counter
#     _end_game() -- Does additional work when the game reaches an end state
#     get_current_player() -- Gets the id of the current player
#     get_player({integer}) -- Gets the player object given the id of the player

class GameTests(unittest.TestCase):
  """Suite to test the functionality of the game

  """

  def test_init(self):
    """Suite to test the init method

    """

    a_players = [Player(1), Player(2)]
    a_x_dist = 10
    a_y_dist = 3
    a_num_to_win = 3
    a_game = Game(a_players, a_x_dist, a_y_dist, a_num_to_win)

    #Check to be sure the board is properly set up
    self.assertEqual(a_game.board, Board(grid=[[0 for _ in range(a_y_dist)] for _ in range(a_x_dist)]))

  def test_play_game(self):
    """Suite to test the play game method

    Runs the game, making sure no exceptions occur

    Then, checks the history, going through each move and checking each move is valid
    
    """

    a_players = [RandomPlayer(1), RandomPlayer(2)]
    a_x_dist = 3
    a_y_dist = 3
    a_num_to_win = 1
    a_game = Game(a_players, a_x_dist, a_y_dist, a_num_to_win)

    #Game is played to competion
    a_game.play_game()

    a_history = a_game.get_history()

    #Go through each move and check to be sure it's valid
    for i in range(1,len(a_history)):
      #Get copy of the board
      prev_board = a_history[i-1]
      cur_board = a_history[i]

      #Check if the board chosen is in valid states
      self.assertTrue(cur_board in bf.get_states(prev_board, a_players[0].get_id()) or cur_board in bf.get_states(prev_board, a_players[1].get_id()),\
        "An invalid board state was added to the history")

      if i == len(a_history) - 1:
        self.assertTrue(bf.check_win(cur_board, a_num_to_win, a_players[0].get_id()) or bf.check_win(cur_board, a_num_to_win, a_players[1].get_id()) or bf.check_tie(cur_board))
      else: 
        self.assertFalse(bf.check_win(cur_board, a_num_to_win, a_players[0].get_id()) or bf.check_win(cur_board, a_num_to_win, a_players[1].get_id()) or bf.check_tie(cur_board))




  def test_get_current_player(self):
    """Suite testing that the current player_id is returned

    """
    
    pass

  def test_get_player(self):
    """Suite testing that the corresponding player given the id is given

    """

    pass

if __name__ == '__main__':
  unittest.main()