// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// This elevator won't let you reach the top of your building.
// Right?

// This Elevator expects to be used from a Building...

interface Building {
    function isLastFloor(uint) external returns (bool);
}

contract Elevator {
    bool public top;
    uint public floor;

    function goTo(uint _floor) public {
        Building building = Building(msg.sender);

        // if not last floor, then:
        if (!building.isLastFloor(_floor)) {
            floor = _floor;
            top = building.isLastFloor(floor);
        }
    }
}
