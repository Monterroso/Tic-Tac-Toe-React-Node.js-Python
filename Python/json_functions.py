import json

"""Utilizes functions for reading and writing from a JSON file

#       to_JSON(object) -- Condenses the object into a JSON object
#       from_JSON(JSON) -- Converts the JSON object into a python object

"""

#A function that writes the object to the json file

#A function that creates the object from the json file
#Needs an attribute to state exactly what type of object it is. 
#Want a function to be able to read a game from file

#Function that turns a board token, or a game token. 

#The game itself contains information, either self containing ais, or ones that wait for a response 

#Game will continue taking turns up until it needs to wait, after doing so, it will then wait and get a response

#Have user_player, which right now will do nothing, but will cause the program to terminate, and it will wait for a response.
# 
# Game itself checks if user_player
# If yes, the game itself stores all of it's info and resturns as a JSON object, you have the turn number and current order

#Game first checks if the player will be a user_player, 

#If game detects this, game will store information as to the turn and who's up
#Returns the game as a JSON, along with current board state, all options, and the id of who's next, all in the JSON
#Don't need to return the history right now
#Game is then recreated when it wants to be brought to life, given command line for that argument for which choice
#When Game is created, the create from JSON is created, given the integer to be the argument to continue for the player
#   