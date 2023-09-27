// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IBuilding {
    function isLastFloor(uint) external returns (bool);
}

contract Attack11 {
    IBuilding building;

    function attack() external {}
}
