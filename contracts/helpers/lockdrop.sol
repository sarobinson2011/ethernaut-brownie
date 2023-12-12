// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*

Title:  LockDrop 

1. time-lock deposit/with contract
2. with an auto airdrop (on withdraw) for every unit time locked

*/

contract LockDrop {
    address public owner;

    mapping (address => timedDeposit) public balance;   // individual account balance

    struct timedDeposit {
        uint256 amount;
        uint256 timestamp;
    }

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        balance[msg.sender] = timedDeposit({
            amount: msg.value, 
            timestamp: block.timestamp
        });
    } 

    function withdraw(uint256 _amount) external {
        // stuff
    }
}


