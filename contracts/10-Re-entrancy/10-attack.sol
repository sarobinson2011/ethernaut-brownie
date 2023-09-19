// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

import "./10-re-entrancy.sol";

contract Attack10 {
    constructor(address _reEntrancyAddress) public payable {
        // upon deployment send funds to Reentrance receive()
        address(_reEntrancyAddress).call{value: msg.value}("");
    }

    receive() external payable {
        // use ReentrantInterface to call withdraw() on Reentrance
        // rinse repeat, until all funds drained
    }
}
