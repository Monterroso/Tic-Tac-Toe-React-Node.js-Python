//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");
let {PythonShell} = require('python-shell')

const app = express();

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
});

//Set the schemas
const GameInfoSchema = new mongoose.Schema ({
  _id: {},
  game: {}
});

const Game = new mongoose.model("game", GameInfoSchema);

function createJSON(jsonString) {
  try {
    let o;
    if (typeof o === "object") {
      o = jsonString;
    }
    else {
      o = JSON.parse(jsonString);
    }

    // Handle non-exception-throwing cases:
    // Neither JSON.parse(false) or JSON.parse(1234) throw errors, hence the type-checking,
    // but... JSON.parse(null) returns null, and typeof null === "object", 
    // so we must check for that, too. Thankfully, null is falsey, so this suffices:
    if (o && typeof o === "object") {
      let keys = Object.keys(o);
      console.log(keys);
      for (let key of keys) {
        o[key] = createJSON(o[key]);
      }
      return o;
    }
  }
  catch (e) { 
    console.log("An error was caught, the error is " + e + "The thing to be parsed was " + jsonString);
  }
  return jsonString;
}


app.get("/", function(req, res) {
  let pyshell = new PythonShell(__dirname + "/public/Python/python_controller.py");
  let gameResult;

  //Recursively recreate the JSON
  pyshell.on('message', function (message) {
    gameResult = message;
  });

  pyshell.end(function (err, code, signal) {
    if (err) throw err;

    currentGame = createJSON(gameResult)["game_json"]["Object"];
    currentBoard = currentGame["board"];
    currentOptions = createJSON(gameResult)["choices"];
    res.render("home", {game: createJSON(gameResult), currentGame: currentGame, currentOptions: currentOptions});
    console.log('finished');
  });
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
})
