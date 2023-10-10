// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./17-recovery.sol";

contract Attack17 {
    // state variables
    Recovery recovery;

    constructor(address _targetAddress) {
        recovery = Recovery(_targetAddress);
    }

    function attack(SimpleToken target) external payable {
        //
    }

    receive() external payable {
        // allows us to receive ether from the selfdestruct function
    }
}
