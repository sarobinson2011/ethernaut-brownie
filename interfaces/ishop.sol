// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IShop {
    function price() external view returns (uint);
    function buy() external;
    function isSold() external;
}
