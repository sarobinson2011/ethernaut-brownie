// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./05-token.sol";

contract Attack05 {
    // state variable - stores an instance of Token
    // contract that we will interact with
    Token tokenContract;

    // constructor takes address of deployed instance
    // of the Telephone contract to attack
    constructor(address _tokenContract) public {
        // allows Attack04 to interact with deployed Telephone contract
        tokenContract = Token(_tokenContract);
    }

    // continue from here
    //  ==> follow video from here
}
