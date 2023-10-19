// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDex {
    function setTokens(address _token1, address _token2) external;
    function addLiquidity(address token_address, uint amount) external;
    function swap(address from, address to, uint amount) external;
    function getSwapPrice(address from, address to, uint amount) 
        external view returns(uint);
    function approve(address spender, uint amount) external;
    function balanceOf(address token, address account) 
        external view returns (uint);
    function token1() view external;
    function token2() view external;
}


