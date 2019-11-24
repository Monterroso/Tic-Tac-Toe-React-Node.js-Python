import json
from game import Game
from player import Player
from user_player import UserPlayer
from random_player import RandomPlayer
from board import Board

"""Utilizes functions for reading and writing from a JSON file

  Functions: 
      game_from_json({JSON}) -- Given a JSON object of a game, converts into game object
      player_from_json({JSON}) -- Given a dictionary of a player, converts into appropriate player
      board_from_json({JSON}) -- Given a JSON object of a board, converts into appropriate board

"""

def game_from_json(json_obj):
  """Converts the game object encoded as a json into a game object and returns it

  Arguments:
    json_obj {JSON} -- encoded Game object we want to decode

  Returns:
    {Game} -- The decoded Game object

  """

  object_json = json.loads(json_obj)

  if object_json["Type"] != "Game":
    raise AttributeError("The json object is not a Game object, it is a {0}".format(object_json["Type"]))

  #Otherwise we know it is a json object
  game_obj = object_json["Object"] 
  x_dist = game_obj["x_dist"]
  y_dist = game_obj["y_dist"]
  turn_number = game_obj["turn_number"]
  max_turns = game_obj["max_turns"]
  num_to_win = game_obj["num_to_win"]
  winner = game_obj["winner"]
  board = board_from(game_obj["board"])
  board_history = [board_from(brd) for brd in game_obj["board_history"]]
  players = [player_from(plr) for plr in game_obj["players"]]

  return Game(players, x_dist, y_dist, num_to_win, turn_start=turn_number,\
     max_turns=max_turns, winner=winner, brd=board, board_history=board_history)


def player_from(dic_obj):
  """Given a player dictionary, converts the dictionary into a player object

  Arguments: 
    dic_obj {dictionary} -- The dictionary representing the player object

  Returns:
    {Player} -- The decoded player object

  """
  if not issubclass(eval(dic_obj["Type"]), Player):
    raise AttributeError("This is not a player dictionary object, it is a {0}".format(dic_obj["Type"]))

  player_obj = dic_obj["Object"]

  player_id = player_obj["player_id"]
  
  return eval(dic_obj["Type"])(player_id)

def board_from(dic_obj):
  """Given a board dictionary, converts the dictionary into a Board object

  Arguments:
    dic_obj {dictionary} -- The dictionary representing the Board object

  Returns:
    {Board} -- The decoded Board object

  """

  if dic_obj["Type"] != "Board":
    raise AttributeError("This is not a Board dictionary object, it is a {0}".format(dic_obj["Type"]))

  #   object_json = dict()
  #   object_json["Type"] = self.__class__.__name__
  #   board_obj = dict()
  #   board_obj["x"] = self.x_dist
  #   board_obj["y"] = self.y_dist
  #   board_obj["grid"] = self.grid
  #   object_json["Object"] = board_obj

  board_obj = dic_obj["Object"]
  x = board_obj["x"]
  y = board_obj["y"]
  grid = board_obj["grid"] 

  return Board(grid=grid)