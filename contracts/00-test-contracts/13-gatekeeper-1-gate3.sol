// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GatekeeperOne3 {
    address public entrant;

    modifier gateThree(bytes8 _gateKey) {
        require(
            uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)),
            "GatekeeperOne: invalid gateThree part one"
        );
        require(
            uint32(uint64(_gateKey)) != uint64(_gateKey),
            "GatekeeperOne: invalid gateThree part two"
        );
        require(
            uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)),
            "GatekeeperOne: invalid gateThree part three"
        );
        _;
    }

    function enter(bytes8 _gateKey) public gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}
