// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

interface ReentrantInterface {
    function donate(address _to) external payable;

    function withdraw(uint _amount) external view;

    function balanceOf(address _who) external view;
}
