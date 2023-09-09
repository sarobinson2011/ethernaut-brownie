// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
    Unlock the vault to beat the level
*/

contract Vault {
    // storage memory slot 0
    bool public locked;
    // storage memory slot 1 (memory storage)
    bytes32 private password;

    constructor(bytes32 _password) {
        locked = true;
        password = _password;
    }

    function unlock(bytes32 _password) public {
        if (password == _password) {
            locked = false;
        }
    }
}
