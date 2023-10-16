// SPDX-License-Identifier: MIT

pragma solidity ^0.5.0;

interface IAlienCodex {
    function owner() view external returns(address);
    function makeContact() external;
    function retract() external;
    function revise(uint i, bytes32 _content) external;
}

// Proess
// 1. check (call) owner 
// 2. call makeContact()
// 3. call retract()
// 4. calculate position 'i'  --> arguement passed to revise()
// 5. call revise(i, player_address)
// 6. check (call) owner


// (include the explanation about the slot storage - slot 0, slot 1)
//        
// the one unknown in the process is the value of 'i' (uint256) 


