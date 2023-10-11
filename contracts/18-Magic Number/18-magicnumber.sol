// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
    set solver = 42 to win

    set this from a contract, using 10 opcodes at most
*/

contract MagicNum {
    address public solver;

    constructor() {}

    function setSolver(address _solver) public {
        solver = _solver;
    }
}

// set and return bytes20(uint160(42)) using inline assembly ??

// decimal 42 = hex 2a

// PUSH20 0x000000000000000000000000000000000000000000000000000000000000002a
// RETURN
