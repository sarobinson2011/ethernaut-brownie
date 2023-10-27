// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Attack23 {
    DexTwo public target;
    address public token3;
    uint256 public token3Balance; 

    constructor(address _target, uint256 _amount) {
        target = DexTwo(_target);
        token3Balance = _amount;
    }

    function attack() public {
        target.swap(from, to, amount);
    }

    receive() external payable {}
}

