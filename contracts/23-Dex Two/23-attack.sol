// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Attack23 {
    DexTwo public target;
    address public token3;
    uint256 public token3Player;
    uint256 public token3Pool; 
    address public owner;

    constructor(address _target, uint256 amountPool, uint256 amountPlayer) {
        owner = msg.sender;
        target = DexTwo(_target);
        token3Pool = amountPool;     // 0 
        token3Player = amountPlayer; // 200
    }

    modifier onlyOwner() {
        require (msg.sender == owner, "Only the owner can withdraw");
        _;
    }

    function attack() public {
        // swap 100 token3 --> 100 token1
        // swap 100 token3 --> 100 token2

        // target.swap(from, to, amount);
    }

    receive() external payable {}

    function withdraw() onlyOwner public {
         msg.sender.transfer(address(this).balance);
     }
}

