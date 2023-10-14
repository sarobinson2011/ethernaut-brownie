// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

// import "../helpers/Ownable-05.sol";
import "/home/oem/Documents/Coding/ethernaut/contracts/helpers/Ownable-05.sol";

contract AlienCodex is Ownable {
//  address private owner;              // slot 0
    bool public contact;                // slot 0
    bytes32[] public codex;             // slot 1

    modifier contacted() {
        assert(contact);
        _;
    }

    function makeContact() public {
        contact = true;
    }

    function record(bytes32 _content) public contacted {
        codex.push(_content);
    }

    function retract() public contacted {
        codex.length--;
    }

    function revise(uint i, bytes32 _content) public contacted {
        codex[i] = _content;
    }
}

// in other words, calling retract() on the empty codex[] array causes
// an underflow:  codex[] --> codex[2^256-1]
// which effectively gives us write access to all of the storage slots
// in the AlienCodex contract.
