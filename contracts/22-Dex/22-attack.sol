// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./22-dex.sol";

contract Attack22 {
    Dex _target;
    address public token1;
    address public token2;
    
    constructor(address _targetAddress) {
        _target = Dex(_targetAddress);
        _target.approve(address(_target), 2 ^ 256); // approve max amount
    }

    function attack() public {
        // 
    }

    receive() external payable {}
}

// Remember:  we need to approve the tokens for swap
// and THEN perform the swaps