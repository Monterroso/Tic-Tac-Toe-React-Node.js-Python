class TicTacToeBoard extends HTMLElement{
  constructor() {
    super();
    
    let width = this.getAttribute('wide');
    let height = this.getAttribute('tall');

    let info = document.createElement("p");

    this.appendChild(info);

    // for(let i = 0; i < width; i++) {
    //   let col = document.createElement('tictactoe-column', {tall: height});
    // }

  }
}

customElements.define('tictactoe-board', TicTacToeBoard);

class TicTacToeColumn extends HTMLElement{
  constructor() {
    super();

    for(let i =0; i < height; i++) {
      let item = document.createElement('tictactoe-item')
    }
    
  }
}

customElements.define('tictactoe-column', TicTacToeColumn);

class TicTacToeItem extends HTMLElement{
  constructor() {
    super();
    let item = document.createElement('p');
    item.innerHTML = "E";
    
  }
}

customElements.define('tictactoe-item', TicTacToeItem);
