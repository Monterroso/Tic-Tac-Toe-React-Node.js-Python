//This creates the board on the page, using board-width and board-height
//Along with the elements to create the given board
let scrip = $('script[id=boardCreator]');

let width = scrip.attr("width");
let height = scrip.attr("height");

let elements = scrip.att("board");

//Get the board
let board = $(".board");

//loop through each column
for(let i = 0; i < width; i++) {
  var col = $("<span></span>");
  board.append(col);
  //loop through each element
  for(let j = 0; j < height; j++) {
    var item = $(`<span>${(i,j)}</span>`);
    col.append(item);
  }
}

//add element and it's classes