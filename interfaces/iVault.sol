// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

interface VaultInterface {
    function locked() external view returns (bool);

    function unlock(bytes32 _password) external;
}
