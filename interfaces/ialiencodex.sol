// SPDX-License-Identifier: MIT

pragma solidity ^0.5.0;

interface IAlienCodex {
    function owner() view external returns(address);
    function contact() view external returns(bool);
    function makeContact() external;
    function retract() external;
    function revise(uint i, bytes32 _content) external;
}




