// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./18-magicnumber.sol";

// create a simple smart contract using bytecode
// bytecode that will deploy a simple contract that always returns 42
// bytes memory bytecode = hex"69602a60005260206000f3600052600a6016f3";

contract Attack18 {
    constructor(MagicNum target) {
        bytes memory bytecode = hex"69602a60005260206000f3600052600a6016f3";
        address addr;
        assembly {
            // create(value, offset, size)
            // Pointer in memeory where code is store at slot 0
            // Dynamic Array (First 32 bytes = Array Length)

            //Size of code:
            // 69602a60005260206000f3600052600a6016f3 = 38 characters
            // Bytecode         = 38 / 2 = 19
            // Bytecode to Hex  = 13
            addr := create(0, add(bytecode, 0x20), 0x13)
        }
        require(addr != address(0));

        target.setSolver(addr);
    }
}
// create(value, offset, size)
// -->
//  --> is a low-level EVM opcode.
// It creates a new contract with the bytecode specified starting from
// the `offset` and of the given `size`. In this case, `value` is set
// to 0 (meaning no Ether is sent along with the contract creation)
