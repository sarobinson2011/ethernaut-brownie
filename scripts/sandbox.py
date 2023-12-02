# from random import choice

# flavours = ["strawberry", "chocolate", "vanilla", "rum raisin", "raspberry ripple"]

# for i in range(10):
#     print(f"ice cream choice = {choice(flavours)}")


""" 
Title:  LockDrop 

1. time-lock deposit/with contract
2. with an auto airdrop (on withdraw) for every unit time locked

// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract LockDrop() {
    // state variables & events
    // mapping - address -> uint256 // balance of each account
    // mapping - address -> uint256 // countdown timer for each account (withdraw / airdrop)

    constructor(uint256 _amount) public payable {
        // initialise
    }

    function deposit() external payable {
        // functionality
    }

    function withdraw() external {
        // functionality
    }

    # need the functionality for the timer
    # 
    # function timeLock()
    
}





"""