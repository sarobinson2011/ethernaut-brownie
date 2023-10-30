// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
import "/home/oem/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.3.2/contracts/token/ERC20";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/*
    Attack philoslophy

    1. any token can be swapped in DexTwo
    2. so we need to use the native DexTwo swap() function
    3. we can mimic the other functions - getSwapPrice() and approve() from here
    4. from, to, amount, spender --> these vars required

*/

contract Attack23 {
    DexTwo public target;
    address public token3;
    address public owner;
    uint256 public token3Player;
    uint256 public token3Pool; 

    constructor(address _target, uint256 amountPool, uint256 amountPlayer) {
        owner = msg.sender;
        target = DexTwo(_target);
        token3Pool = amountPool;     // 0 
        token3Player = amountPlayer; // 200
    }


    // function getSwapAmount(address from, address to, uint amount) public view returns(uint)
    // function approve(address spender, uint amount) public


    function attack() public {
        // check GOHEESHENG
  
        // swap 100 token3 --> 100 token1
        // swap 100 token3 --> 100 token2

        // target.swap(from, to, amount);
    }

    receive() external payable {}

    modifier onlyOwner() {
        require (msg.sender == owner, "Only the owner can withdraw");
        _;
    }

    function withdraw() onlyOwner public {
         msg.sender.transfer(address(this).balance);
     }
}

