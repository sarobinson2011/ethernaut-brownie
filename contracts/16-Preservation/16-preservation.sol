// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
    The goal of this level is for you to claim ownership of 
    the instance you are given.

1)  Look into Solidity's documentation on the delegatecall low level 
    function, how it works, how it can be used to delegate operations 
    to on-chain libraries, and what implications it has on execution scope.
    
2)  Understand what it means for delegatecall to be context-preserving.

*/

contract Preservation {
    // public library contracts
    address public timeZone1Library; // storage slot 0
    address public timeZone2Library; // storage slot 1
    address public owner; //            storage slot 2  <-- THIS
    uint storedTime;
    // Sets the function signature for delegatecall
    bytes4 constant setTimeSignature = bytes4(keccak256("setTime(uint256)"));

    constructor(
        address _timeZone1LibraryAddress,
        address _timeZone2LibraryAddress
    ) {
        timeZone1Library = _timeZone1LibraryAddress;
        timeZone2Library = _timeZone2LibraryAddress;
        owner = msg.sender;
    }

    // set the time for timezone 1
    function setFirstTime(uint _timeStamp) public {
        timeZone1Library.delegatecall(
            abi.encodePacked(setTimeSignature, _timeStamp)
        );
    }

    // set the time for timezone 2
    function setSecondTime(uint _timeStamp) public {
        timeZone2Library.delegatecall(
            abi.encodePacked(setTimeSignature, _timeStamp)
        );
    }
}

// Simple library contract to set the time
contract LibraryContract {
    // stores a timestamp
    uint storedTime;

    function setTime(uint _time) public {
        storedTime = _time;
    }
}
