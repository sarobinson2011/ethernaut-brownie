// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
    Set entrant = to player.address... and you win  :-0
*/

contract GatekeeperOne {
    address public entrant;

    // Gate One - pass by using a proxy contract
    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }

    // Gate Two - pass by ensuring gasleft() is an
    // integer multiple of 8191 - brute force attack this one
    modifier gateTwo() {
        require(gasleft() % 8191 == 0);
        _;
    }

    // Gate Three - pass by correctly generating the key
    modifier gateThree(bytes8 _gateKey) {
        require(
            uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)),
            "GatekeeperOne: invalid gateThree part one"
        );
        require(
            uint32(uint64(_gateKey)) != uint64(_gateKey),
            "GatekeeperOne: invalid gateThree part two"
        );

        // uint160 is the shortest unint which can hold 20 bytes of data.
        // Ethereum addresses are 20 bytes long in hexadecimal format.
        // which converts an Ethereum address directly into uint160 and back.
        require(
            uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)),
            "GatekeeperOne: invalid gateThree part three"
        );
        _;
    }

    function enter(
        bytes8 _gateKey
    ) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}
