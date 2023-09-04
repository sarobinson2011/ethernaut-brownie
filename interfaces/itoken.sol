pragma solidity ^0.6.0;

// 'TokenInterface' allows you to interact with the 'Token' contract
interface TokenInterface {
    function transfer(address _to, uint _value) external returns (bool);

    function balanceOf(address _owner) external view returns (uint balance);
}
