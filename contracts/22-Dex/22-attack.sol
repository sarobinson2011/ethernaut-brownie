// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./22-dex.sol";

contract Attack22 {
    Dex target;

    constructor(address _targetAddress) {
        target = Dex(_targetAddress);
    }

    function attack() public {
        // stuff
    }

    receive() external payable {
        // stuff
    }
}

