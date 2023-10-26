// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";

contract Attack23 {
    DexTwo public target;
    address public token3;

    constructor(address _target, uint256 _amount) {
        target = DexTwo(_target);
        token3 = _amount;
    }

    function attack() public {
        //
    }

    receive() external payable {}
}
