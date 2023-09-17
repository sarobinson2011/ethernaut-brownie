// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

import "./10-re-entrancy.sol";

contract Attack10 {
    // constructor sets the address of the Reentrancy contract to attack
    constructor(address _reEntrancyAddress) public payable {
        // #ToDo
        // need to fund Reentrance, by call donate upon deployment
    }

    receive() external payable {
        // use ReentrantInterface to call withdraw() on Reentrance
        // rinse repeat, until all funds drained
    }
}
