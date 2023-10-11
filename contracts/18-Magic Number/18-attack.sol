// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./18-magicnumber.sol";

// contract Attack18 {
//     function attack() external pure returns (address) {
//         address magicNumber;
//         assembly {
//             magicNumber := 0x000000000000000000000000000000000000000000000000000000000000002a
//         }
//         return magicNumber;
//     }
// }

contract Attack18 {
    // state variables
    MagicNum public magicNum;

    constructor(address _targetAddress) {
        magicNum = MagicNum(_targetAddress);
    }

    function attack(address _solver) external pure returns (address) {
        return _solver;
    }
}
