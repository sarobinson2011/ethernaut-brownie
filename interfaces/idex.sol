// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDex {
    function setTokens(address _token1, address _token2) external;//        onlyOwner
    function addLiquidity(address tokenAddress, uint amount) external;//    onlyOwner
    function getSwapPrice(address from, address to, uint amount) 
        external view returns(uint);//                                      swap price     (view)

    function approve(address spender, uint amount) external;//             - approve token
    function swap(address from, address to, uint amount) external;//       - swap token
    
    function balanceOf(address token, address account)//                    token balance  (view) 
        external view returns (uint);                                     
    function token1() view external;//                                      token1 address (view)
    function token2() view external;//                                      token2 address (view)
}


