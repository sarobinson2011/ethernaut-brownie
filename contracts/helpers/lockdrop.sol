// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*

Title:  LockDrop 

1. time-lock deposit/with contract
2. with an auto airdrop (on withdraw) for every unit time locked

*/

contract LockDrop {
    address public owner;
    mapping (address => uint256) public balance; // balance of each account

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        balance[msg.sender] += msg.value;
    } 

    function withdraw(uint256 _amount) external {
        require(balance[msg.sender] >= _amount, "Insuffienct funds, sorry...");
        balance[msg.sender] -= _amount;
        payable(msg.sender).transfer(_amount);
    }



    // need the functionality for the timer
    // 
    // function timeLock()   
}


