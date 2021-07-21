//jshint esversion:6

function setTicTacToeBorderClasses(x, y, maxX, maxY) {
    let retString = "";

    x === 0 && (retString += "left-border");
    x === (maxX - 1) && (retString += "right-border");

    y === 0 && (retString += "top-border");
    y === (maxY - 1) && (retString += "bottom-border");

    return retString;

}