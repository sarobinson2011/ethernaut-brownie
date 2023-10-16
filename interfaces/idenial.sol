// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDenial {
    function partner() external;
    function owner() external returns(address);
    function timeLastWithdrawn() external;
    function setWithdrawPartner(address _partner) external;
    function withdraw() external;
    function contractBalance() external view returns (uint);
}
