import sys 
import json
from game import Game
from user_player import UserPlayer
from random_player import RandomPlayer
from json_functions import game_from_json

import unittest


"""Given command line arguments, this will run a game


""" 

def new_game():
  return_object = dict()

  player_1 = UserPlayer(1)
  player_2 = RandomPlayer(2)
  players = [player_1, player_2]
  x_dist = 3
  y_dist = 3
  num_to_win = 2
  new_game = Game(players, x_dist, y_dist, num_to_win)

  game_json = new_game.play_game()

  choices = [board.to_json() for board in new_game.board.get_states(new_game.get_current_player())]
  
  is_over = new_game.is_game_over()

  winner = new_game.winner

  return_object["game_json"] = game_json
  return_object["choices"] = choices
  return_object["is_over"] = is_over
  return_object["winner"] = winner

  return json.dumps(return_object)

def continue_game(game_json, choice):
  return_object = dict()

  created_game = game_from_json(game_json)

  choice = int(choice)

  player = created_game.get_player(created_game.get_current_player())
  player.set_choice(choice)

  game_json = created_game.play_game()

  choices = [board.to_json() for board in created_game.board.get_states(created_game.get_current_player())]
  
  is_over = created_game.is_game_over()

  winner = created_game.winner

  return_object["game_json"] = game_json
  return_object["choices"] = choices
  return_object["is_over"] = is_over
  return_object["winner"] = winner

  return json.dumps(return_object)

class ControllerTests(unittest.TestCase):
  """We check to be sure that the controller behaves as we expect it to

  """

  def test_new_game(self):
    """Testing suite to start a new game

    """

    #Just check manually that the game json object is printed
    print(new_game())

  def test_continue_game(self):
    """Testing suite to continue game

    """

    a_player_1_id = 1
    a_player_2_id = 2
    a_players = [UserPlayer(a_player_1_id), RandomPlayer(a_player_2_id)]
    a_x_dist = 3
    a_y_dist = 3
    a_num_to_win = 2
    a_game = Game(a_players,a_x_dist,a_y_dist,a_num_to_win)
    a_game_json = a_game.play_game()

    #Just check that the game itself seems to work
    print(continue_game(a_game_json, 0))

    
if __name__ == "__main__":
    # unittest.main()

    if len(sys.argv) == 1:
      #We need to create a new game
      print(new_game())
        
    if len(sys.argv) == 3:
      #A game and a player choice have been given
      print(continue_game(sys.argv[1], sys.argv[2]))