// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./13-gatekeeper-1-gate3.sol";

contract Attack13_gate3 {
    bytes8 public gateKey;
    uint public gasAmount;
    GatekeeperOne3 public target;

    constructor(address _targetAddress) {
        target = GatekeeperOne3(_targetAddress);
    }

    function attack(bytes8 _gateKey) external {
        gateKey = _gateKey;
        target.enter(gateKey);
    }
}

/*
    To pass Gate 3 find gateKey:

    Solution --> First 20 digits of player EOA, with the following bitmask:

    bytes8 first16 = "0x555FCDdD6035699deE25";
    bytes8 gateKey = first16 & 0xFFFFFFFF0000FFFF;
*/

// 'bit masking' operation:
// where F is 'show'
// where 0 is mask

/*  0xCDdD6035699deE25
    0xFFFFFFFF0000FFFF
    ------------------
 =  0xCDdD60350000eE25      <-- the gateKey  
*/

// MS-half: F8f8269488f73fab3935
// LS-half: 555FCDdD6035699deE25
