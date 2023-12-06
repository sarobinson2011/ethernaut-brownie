// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*

Title:  LockDrop 

1. time-lock deposit/with contract
2. with an auto airdrop (on withdraw) for every unit time locked

*/

contract LockDrop {
    // state variables & events
    uint256 public owner;
    mapping (address => uint256) balanceOf; // balance of each account
    // mapping - address -> uint256 // countdown timer for each account (withdraw / airdrop)

    constructor(uint256 _amount) public {
        // initialise
    }

    function deposit(uint256 _amount) external payable {
        // balanceOf(msg.sender) += msg.value;
    }

    //  

    function withdraw(uint256 _amount) external {
        // require(_amount <= balanceOf(msg.sender));
        // (bool success, ) = call();
    }

    // need the functionality for the timer
    // 
    // function timeLock()   
}


