// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

interface KingInterface {
    function prize() external view returns (uint);

    function _king() external view returns (address payable);
}
