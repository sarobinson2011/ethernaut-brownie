// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet target;

    constructor(address _targetAddress) {
        target = PuzzleWallet(_targetAddress);
    }

    function attack() public {
        // multicall attack
    }
}