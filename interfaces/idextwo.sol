// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDexTwo {
    function swap(address from, address to, uint amount) external;
    function getSwapAmount(address from, address to, uint amount) external view returns(uint);
    function approve(address spender, uint amount) external;
    function balanceOf(address token, address account) external view returns (uint);
}


