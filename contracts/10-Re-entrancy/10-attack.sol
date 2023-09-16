// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

contract Attack10 {
    // constructor sets the address of the Reentrancy contract to attack
    constructor(address _reEntrancyAddress) public payable {
        // #ToDo
    }

    receive() external payable {
        // call withdraw(_amount) on Reentrance
        // NEXT...
        // use ReentrantInterface to call withdraw() on Reentrance
        // rinse repeat, until drained
    }
}
