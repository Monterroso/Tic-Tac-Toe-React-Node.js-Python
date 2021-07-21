import React from "react";
import Header from "./Header.jsx";
import Footer from "./Footer.jsx"

function App(props) {

    const currentBoard = props.currentBoard;
    const currentOptions = props.currentOptions;

    return (
        <div>
            <Header />

            <h1>Hello there!</h1>

            <p>This is the current board is {currentBoard}</p>

            <p>Here are all the possible board options</p>

            {currentOptions.map(element => (<p>
                    {element}
                </p>)
            )}

            <form action="/" method="post">
                <input type="text"></input>
            </form>
        </div>
        
        

    )
}

export default App;
