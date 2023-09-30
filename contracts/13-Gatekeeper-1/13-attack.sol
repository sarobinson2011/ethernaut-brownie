// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./13-gatekeeper-1.sol";

contract Attack13 {
    bytes8 public gateKey;
    GatekeeperOne public target;

    constructor(address _targetAddress) {
        target = GatekeeperOne(_targetAddress);
    }

    function attack(bytes8 _gateKey) external {
        target.enter(_gateKey);
    }
}
