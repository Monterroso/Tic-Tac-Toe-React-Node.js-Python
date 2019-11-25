//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");
const pythonShell = require("python-shell");

const app = express()

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

//Mongoose set up
mongoose.connect('mongodb://localhost:27017/tictactoeDB',
 {
  useUnifiedTopology: true,
  useNewUrlParser: true
})
.catch((err) => {
  console.log(err);
})

// self.x_dist = x_dist
//     self.y_dist = y_dist

//     self.turn_number = turn_start
//     if brd == None:
//       self.board = Board(x_dist, y_dist)
//     else:
//       self.board = brd
//     if board_history == None:
//       self.board_history = [self.board]
//     else: 
//       self.board_history = board_history
//     self.num_to_win = num_to_win

//     self.max_turns = max_turns

//     self.winner = winner


//Set the schemas
const GameInfoSchema = new mongoose.Schema ({
  game: GameSchema
});

const GameSchema = new mongoose.Schema ({
  players: [PlayerSchema],
  x_dist: {type: Number, min: 1},
  y_dist: {type: Number, min: 1},
  turn_number: {type: Number, min: 0}, 
  num_to_win: {type: Number, min: 0},
  max_turns: {type: Number, min: 0},
  winner: {type: Number, min: -1},
  board: BoardSchema,
  board_history: [BoardSchema]
});

const BoardSchema = new mongoose.Schema({
  x_dist: {type: Number, min: 1},
  y_dist: {type: Number, min: 1},
  grid: [[int]]
});

const PlayerSchema = new mongoose.Schema ({
  type: String,
  playerID: {type: Number, min: 1}
})

const Task = mongoose.model("Game", ItemSchema);

app.get("/", function(req, res) {
  res.render("home")
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
})
