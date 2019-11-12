import board
import player


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
    get_states(integer) -- Gets all possible states for a given player
    check_win(integer) -- Checks if the player is in a win state (only horizontal and vertical)
    check_tie() -- Checks if current state is in a tie state (only if the board is completely filled)
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

  #####################         ##################### 
  #                    Play Game                    #
  #####################         ##################### 

  def play_game(self):
    """Plays the tic-tac-toe game to completion

    """ 
    cur_player = self.get_current_player()

    #Loop game until completion
    while self.turn_number <= self.max-turns:

      #Store board at current counter
      self.board_history.append(self.board)

      #Check for win or tie
        #If either, call end game with respective parameters
      if check_win(cur_player):
        self._end_game(self, cur_player)
        break
      if check_tie():
        self._end_game(self)
        break


      #Incriment turn counter
      _increment_turn()

      #Get current player
      cur_player = self.get_current_player()

      player_object = self.get_player(cur_player)

      #Get board states for current player
      chosen_board = player_object.choose_state(self.get_states(cur_player))

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
    if winner_id is not None: 
      print("Player {0} has won the game!".format(winner_id))
    else: 
      print("No one won, it was a cat's game!")

  #####################         ##################### 
  #                    Utilities                    #
  #####################         ##################### 

  def get_states(self, player_id):
    """Returns all possible game states the player can make

    Arguments:
      player_id {integer} -- The id of the player
  
    Returns:
      {list of (Board)} -- The list of Boards that the player can branch to
    """

    boards = []

    #Double for loop through x and y coordinates
    for i in range(self.x_dist):
      for j in range(self.y_dist):
        #check if space is free
          #if free, dupblicate board, add id to location
          #add board to boards
        if self.board.get_at(i, j) == 0:
          new_board = self.board.copy()
          new_board.place_at(player_id, (i, j))
          boards.append(new_board)

    #return boards
    return boards


  def check_win(self, player_id):
    """Checks if this player has won

    Arguments:
      player_id {integer} -- The id of the player we are checking

    Returns: 
      {boolean} -- Returns true if the player has won, false if they have not

    """

    #Row Check
    for x in range(self.x_dist):
      counter = 0
      for y in range(self.y_dist):
        if self.board.get_at(x,y) == player_id:
          counter += 1
        else: 
          counter = 0

        if counter == self.num_to_win: 
          return True

    #Column Check
    for y in range(self.x_dist):
      counter = 0
      for x in range(self.y_dist):
        if self.board.get_at(x,y) == player_id:
          counter += 1
        else: 
          counter = 0

        if counter == self.num_to_win: 
          return True

    #If hasn't returned true, then it's false
    return False

  def check_tie(self):
    """Checks if there is no way a player can win, currently returns true if and only if the board is filled

    Returns:
      {boolean} -- Returns true if the player is not able to win, false if they still can. 

    """

    for i in range(self.x_dist):
      for j in range(self.y_dist):
        if self.board.get_at(x,y) != player_id:
          return False

    return True

  def get_current_player(self):
    """Returns the id of the current player 

    Returns:
      {integer} -- The id of the current player
    
    """

    return self.players[self.turn_number - 1 % len(self.players)]

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

    raise Exception("A player with the given id was not found in the player list")
