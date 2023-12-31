// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

interface IPuzzleWallet {
    // Puzzle Wallet
    function owner() external view;
    function maxBalance() external view;
    function init(uint256 _maxBalance) external;
    function setMaxBalance(uint256 _maxBalance) external;
    function addToWhitelist(address addr) external;
    function deposit() external payable;
    function execute(address to, uint256 value, bytes calldata data) external payable;
    function multicall(bytes[] calldata data) external payable;
    // Puzzle Proxy
    function proposeNewAdmin(address _newAdmin) external;  
    function whitelisted(address _addr) external view returns (bool);
}
