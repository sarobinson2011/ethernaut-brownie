// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// set top == true to beat the level

interface Building {
    // should have been a view function
    function isLastFloor(uint) external returns (bool);
}

contract Elevator {
    // false
    bool public top;
    // 0
    uint public floor;

    function goTo(uint _floor) public {
        Building building = Building(msg.sender);

        if (!building.isLastFloor(_floor)) {
            floor = _floor;
            top = building.isLastFloor(floor);
        }
    }
}
