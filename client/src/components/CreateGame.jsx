import React, { useState, useEffect } from "react";

// SERVICES
import gameService from '../services/gameService';

// COMPONENTS
import Navbar from "./Navbar.jsx";

//ELEMENTS
import Button from '@material-ui/core/Button';

import uuidv1 from "uuid";
import { navigate } from "hookrouter";

function FriendPage() {

  const [friends, setFriends] = useState([]);

  const [gameInputs, setGameInputs] = useState({
    dim1: 1,
    dim2: 1,
    winamount: 1,
    diagnals: false,
    otherUser: "",
    amIFirst: false
  });

  // useEffect(() => {
  //   getFriends();
  // });

  //if user is already logged in then go to login
  useEffect(() => {
    gameService.checkLogin(isLoggedIn => !isLoggedIn && navigate("/login"));
    getFriends();
  }, []);

  const getFriends = async () => {
    let res = await gameService.getMe(()=>{});
    console.log("This is the friend list " + JSON.stringify(res));
    setFriends(res.friendList);
  };

  const renderFriends = friend => {
    return (
      {friend}
    );
  };

  const createGame = (event) => {
    event.preventDefault();
    console.log(gameInputs);
  }

  const updateField = (field, value, isCheck) => {
    console.log(`There was a change, field was ${field} and value was ${value}`)
    
    setGameInputs((prev) => {
      if (isCheck) {
        value = !prev[field];
      }
      return {
        ...prev,
        [field]: value
      }
    })
  }

  return (
    <div className="CreateGame">
      <Navbar></Navbar>
      <form className="GameParamters" onSubmit={createGame}>
        <div className="block-segment">
          <label>Dimension 1</label>
          <input 
          onChange={event => {updateField(event.target.name, event.target.value)}} 
          type="number" 
          name="dim1"
          min="1"
          value={gameInputs["dim1"]}/>
          <br/>
        </div>
        <div className="block-segment">
          <label>Dimension 2</label>
          <input 
          onChange={event => {updateField(event.target.name, event.target.value)}} 
          type="number" 
          name="dim2" 
          min="1"
          value={gameInputs["dim2"]}/>
          <br/>
        </div>
        <div className="block-segment">
          <label>Win amount</label>
          <input 
          onChange={event => {updateField(event.target.name, event.target.value)}} 
          type="number" 
          name="winamount"
          min="1"
          value={gameInputs["winamount"]}/>
          <br/>
        </div>
        <div className="block-segment">
          <label>Diagnals allowed?</label>
          <input 
          onChange={event => {updateField(event.target.name, event.target.value, true)}} 
          type="checkbox" 
          name="diagnals"
          value={gameInputs["diagnals"]}/>
          <br/>
        </div>
        <div className="block-segment">
          <label>Select Opponent</label>
          {friends.length > 0? 
          <select 
          onChange={event => {updateField(event.target.name, event.target.value)}} 
          name="otherUser"
          value={gameInputs["otherUser"]}>
            {friends.map(friend => <option key={uuidv1()} value={friend}>{friend}</option>)}
          </select>:
          <p>You need to add friends before you can create a game</p>}
          <br/>
        </div>
        <div className="block-segment">
          <label>Am I first?</label>
          <input 
          onChange={event => {updateField(event.target.name, event.target.value, true)}} 
          type="checkbox" 
          name="amIFirst"
          value={gameInputs["amIFirst"]}/>
          <br/>
        </div>
        <div className="block-segment">
          <input 
          type="submit" 
          value="Create Game!"/>
          <br/>
        </div>
      </form>
    </div>
    
  );
}

export default FriendPage;