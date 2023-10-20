// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./22-dex.sol";

contract Attack22 {
    Dex _target;

    constructor(address _targetAddress) {
        _target = Dex(_targetAddress);
    }

    function attack() public {
        // stuff
    }

    receive() external payable {}
}


// <><><><><><><>       need to fuck with the swap price       <><><><><><><> 
//
// 
// uint swapAmount = getSwapPrice(from, to, amount);
// 
// function getSwapPrice(address from, address to, uint amount) public view returns(uint){
//    return((amount * IERC20(to).balanceOf(address(this)))/IERC20(from).balanceOf(address(this)));
// }
// 
// -->  fuck around with the token1 and token2 addresses (in the storage slots) ???