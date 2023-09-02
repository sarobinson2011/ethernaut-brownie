// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./05-token.sol";

contract Attack05 {
    Token tokenContract;

    constructor(address _tokenContract) public {
        tokenContract = Token(_tokenContract);
    }
}

/*

// import 'interfaces/Itoken.sol';

contract Attack05 {
  address public owner;

  constructor() public {
    owner = msg.sender;
  }
}
*/
