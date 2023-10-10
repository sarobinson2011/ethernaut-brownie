// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ISimpleToken {
    function transfer(address _to, uint _amount) external;

    function destroy(address payable _to) external;
}
