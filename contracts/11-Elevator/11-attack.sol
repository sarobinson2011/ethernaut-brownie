// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IElevator {
    function goTo(uint) external returns (bool);
}

contract Attack11 {
    function attack(address _target) external {
        IElevator elevator = IElevator(_target);

        elevator.goTo(1);
    }
}
